import os
import json
from dotenv import load_dotenv
from ai_generator import DataExtractor

# Tải biến môi trường từ file .env
load_dotenv()

def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("[-] Lỗi: Không tìm thấy biến môi trường GEMINI_API_KEY.")
        print("[-] Hãy tạo file .env ở thư mục gốc và thêm: GEMINI_API_KEY=your_key_here")
        return

    test_file_path = "sample_product.md"
    
    if not os.path.exists(test_file_path):
        print(f"[-] Lỗi: Không tìm thấy file '{test_file_path}'")
        return
        
    with open(test_file_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
        
    print("[*] Đang khởi tạo bộ bóc tách dữ liệu AI (Gemini)...")
    extractor = DataExtractor()
    
    print("[*] Đang gửi nội dung Markdown cho LLM phân tích. Vui lòng đợi...")
    try:
        product_data = extractor.extract_product_info(markdown_content)
        
        print("[+] Trạng thái: THÀNH CÔNG\n")
        print("=== KẾT QUẢ JSON ĐÃ TRÍCH XUẤT ===")
        print(product_data.model_dump_json(indent=2))
        print("==================================")
    except Exception as e:
        print(f"[-] Lỗi trong quá trình trích xuất: {e}")

if __name__ == "__main__":
    main()
