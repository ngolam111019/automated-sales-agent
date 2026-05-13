import os
from google import genai
from pydantic import BaseModel
from .schemas import ProductData

class DataExtractor:
    def __init__(self):
        # google-genai client sẽ tự động tìm biến môi trường GEMINI_API_KEY
        self.client = genai.Client()
        # Khuyên dùng gemini-1.5-flash cho tác vụ xử lý text tốc độ cao & giá rẻ
        self.model_name = 'gemini-2.5-flash'

    def extract_product_info(self, markdown_text: str) -> ProductData:
        prompt = f"""
Bạn là một trợ lý ảo chuyên phân tích dữ liệu sản phẩm.
Dưới đây là nội dung Markdown được cào từ một trang web thương mại điện tử.
Hãy trích xuất chính xác tên sản phẩm, giá gốc, giá khuyến mãi (nếu có), các thông số kỹ thuật và tính năng nổi bật.
Trường hợp không tìm thấy thông tin nào đó, hãy để null hoặc mảng/chuỗi rỗng.

NỘI DUNG MARKDOWN:
{markdown_text}
"""
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ProductData,
                temperature=0.1 # Để kết quả ổn định và ít tính sáng tạo
            ),
        )
        
        # Parse chuỗi JSON trả về thành đối tượng Pydantic
        return ProductData.model_validate_json(response.text)
