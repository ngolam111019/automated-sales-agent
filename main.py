import asyncio
import time
import schedule
import logging
from datetime import datetime
from dotenv import load_dotenv

from crawler import ProductScraper
from ai_generator import DataExtractor
from ai_generator.content_generator import ContentGenerator
from database.db_session import init_db, SessionLocal
from database.repository import ProductRepository

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# Danh sách URL để cấu hình
OUR_PRODUCT_URL = "https://tiki.vn/dien-thoai-samsung-galaxy-a17-lte-8-128gb-kinh-cuong-luc-gorilla-victus-camera-50mp-ios-ai-gemini-hang-chinh-hang-p278505394.html"
COMPETITOR_PRODUCT_URL = "https://tiki.vn/dien-thoai-oppo-a60-8gb-128gb-hang-chinh-hang-p273418187.html"

async def process_product(url: str, scraper: ProductScraper, extractor: DataExtractor, repo: ProductRepository, db_session):
    logger.info(f"Đang thu thập dữ liệu từ: {url}")
    crawl_result = await scraper.scrape_product(url)
    
    if not crawl_result.get("success"):
        logger.error(f"Crawling thất bại cho URL: {url}")
        return None
        
    markdown_content = crawl_result.get("markdown_content", "")
    logger.info(f"Crawl thành công. Đang bóc tách dữ liệu AI...")
    
    try:
        product_data = extractor.extract_product_info(markdown_content)
        logger.info(f"Bóc tách thành công: {product_data.product_name}")
        
        # Lưu vào database
        saved_product = repo.save_product_data(product_data, url=url)
        logger.info(f"Đã lưu vào Database ID: {saved_product.id}")
        return saved_product
    except Exception as e:
        logger.error(f"Lỗi khi bóc tách hoặc lưu dữ liệu: {e}")
        return None

async def run_pipeline():
    logger.info("=== BẮT ĐẦU LUỒNG TỰ ĐỘNG HÓA ===")
    
    # 1. Khởi tạo Database
    init_db()
    db = SessionLocal()
    repo = ProductRepository(db)
    
    # 2. Khởi tạo các công cụ
    scraper = ProductScraper(headless=True)
    extractor = DataExtractor()
    content_gen = ContentGenerator()
    
    try:
        # 3. Xử lý sản phẩm của mình
        our_product = await process_product(OUR_PRODUCT_URL, scraper, extractor, repo, db)
        
        # 4. Xử lý sản phẩm đối thủ
        competitor_product = await process_product(COMPETITOR_PRODUCT_URL, scraper, extractor, repo, db)
        
        # 5. Sinh bài PR So sánh
        if our_product and competitor_product:
            logger.info("Đang sinh bài PR so sánh tự động...")
            pr_content = content_gen.generate_comparison_pr(our_product, competitor_product)
            
            # Lưu bài PR
            import os
            os.makedirs("reports", exist_ok=True)
            filename = os.path.join("reports", f"PR_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(pr_content)
            logger.info(f"Hoàn thành! Bài PR đã được lưu tại: {filename}")
        else:
            logger.warning("Không thể sinh bài PR vì thiếu dữ liệu sản phẩm.")
            
    finally:
        db.close()
        logger.info("=== KẾT THÚC LUỒNG TỰ ĐỘNG HÓA ===\n")

def job():
    asyncio.run(run_pipeline())

def main():
    logger.info("Hệ thống Automated Sales Agent đã khởi động.")
    
    # Bạn có thể điều chỉnh lịch trình ở đây
    # Ví dụ: Chạy mỗi ngày vào lúc 08:00 sáng
    schedule.every().day.at("08:00").do(job)
    
    # Để test ngay lập tức, chúng ta sẽ gọi job() một lần
    logger.info("Đang chạy thử nghiệm lần đầu tiên...")
    job()
    
    logger.info("Đã lên lịch chạy định kỳ. Nhấn Ctrl+C để thoát.")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
