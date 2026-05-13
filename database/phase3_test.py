import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_session import init_db, SessionLocal
from database.repository import ProductRepository
from database.models import Product, Specification, Feature
from ai_generator.content_generator import ContentGenerator
from ai_generator.schemas import ProductData, SpecificationItem
from dotenv import load_dotenv

load_dotenv()

def create_mock_competitor():
    return ProductData(
        product_name="Điện thoại OPPO A60 8GB/128GB",
        original_price=5490000,
        discounted_price=4490000,
        specifications=[
            SpecificationItem(name="RAM", value="8GB"),
            SpecificationItem(name="Bộ nhớ trong", value="128GB"),
            SpecificationItem(name="Kính cường lực", value="Panda Glass"),
            SpecificationItem(name="Camera", value="50MP"),
            SpecificationItem(name="Hệ điều hành", value="Android 14"),
            SpecificationItem(name="Kết nối", value="LTE")
        ],
        key_features=[
            "Sạc siêu nhanh SuperVOOC 45W",
            "Màn hình tần số quét 90Hz",
            "Thiết kế mỏng nhẹ"
        ]
    )

def main():
    print("[*] Khởi tạo Database PostgreSQL...")
    init_db()
    
    db = SessionLocal()
    repo = ProductRepository(db)
    
    samsung_data = ProductData(
        product_name="Điện Thoại Samsung Galaxy A17 LTE (8/128GB)",
        original_price=5190000,
        discounted_price=4190000,
        specifications=[
            SpecificationItem(name="RAM", value="8GB"),
            SpecificationItem(name="Bộ nhớ trong", value="128GB"),
            SpecificationItem(name="Kính cường lực", value="Gorilla Victus"),
            SpecificationItem(name="Camera", value="50MP"),
            SpecificationItem(name="Hệ điều hành", value="IOS"),
            SpecificationItem(name="AI", value="Gemini"),
            SpecificationItem(name="Kết nối", value="LTE")
        ],
        key_features=[
            "Kính Cường Lực Gorilla Victus",
            "Camera 50MP",
            "AI Gemini",
            "Hàng Chính Hãng"
        ]
    )
    
    print("[*] Lưu Samsung A17 vào DB...")
    p1 = repo.save_product_data(samsung_data, url="https://tiki.vn/samsung-a17")
    
    print("[*] Lưu sản phẩm đối thủ (OPPO A60) vào DB...")
    oppo_data = create_mock_competitor()
    p2 = repo.save_product_data(oppo_data, url="https://tiki.vn/oppo-a60")
    
    print(f"[+] Lấy từ DB thành công: P1={p1.name}, P2={p2.name}")
    
    print("\n[*] Kích hoạt AI Content Generator...")
    generator = ContentGenerator()
    try:
        pr_article = generator.generate_comparison_pr(our_product=p1, competitor_product=p2)
        print("\n" + "="*50)
        print("BÀI PR ĐƯỢC TẠO TỰ ĐỘNG BẰNG AI:\n")
        print(pr_article)
        print("="*50)
        
        with open("sample_pr.md", "w", encoding="utf-8") as f:
            f.write(pr_article)
            
    except Exception as e:
        print(f"[-] Lỗi sinh PR: {e}")

if __name__ == "__main__":
    main()
