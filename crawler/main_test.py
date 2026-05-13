import asyncio
from crawler import ProductScraper

async def main():
    test_url = "https://tiki.vn/dien-thoai-samsung-galaxy-a17-lte-8-128gb-kinh-cuong-luc-gorilla-victus-camera-50mp-ios-ai-gemini-hang-chinh-hang-p278505394.html"
    
    print(f"[*] Bắt đầu crawl dữ liệu từ: {test_url}")
    scraper = ProductScraper(headless=True)
    
    result = await scraper.scrape_product(test_url)
    
    if result.get("success"):
        print("[+] Trạng thái: THÀNH CÔNG")
        print(f"[+] Status Code: {result['status_code']}")
        
        markdown = result.get("markdown_content", "")
        with open("sample_product.md", "w", encoding="utf-8") as f:
            f.write(markdown)
            
        print("[+] Đã lưu toàn bộ nội dung markdown vào file 'sample_product.md'")
    else:
        print("[-] Trạng thái: THẤT BẠI")

if __name__ == "__main__":
    asyncio.run(main())
