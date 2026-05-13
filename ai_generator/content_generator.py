import os
from google import genai
from database.models import Product

class ContentGenerator:
    def __init__(self):
        self.client = genai.Client()
        self.model_name = 'gemini-2.5-flash'

    def generate_comparison_pr(self, our_product: Product, competitor_product: Product) -> str:
        prompt = f"""
Bạn là một chuyên gia Copywriter công nghệ xuất sắc.
Hãy viết một bài PR/So sánh giữa 2 sản phẩm điện thoại dưới đây.
Sản phẩm của chúng ta là: "{our_product.name}".
Sản phẩm của đối thủ là: "{competitor_product.name}".

Mục tiêu: Đưa ra so sánh khách quan nhưng khéo léo làm nổi bật ưu điểm của sản phẩm chúng ta (về giá, thông số, hoặc tính năng). Viết theo phong cách thân thiện, thu hút, chuẩn SEO.

--- THÔNG TIN SẢN PHẨM CỦA CHÚNG TA ---
Tên: {our_product.name}
Giá gốc: {our_product.original_price or 'Không có'}
Giá khuyến mãi: {our_product.discounted_price or 'Không có'}
Thông số:
{self._format_specs(our_product)}
Tính năng:
{self._format_features(our_product)}

--- THÔNG TIN SẢN PHẨM ĐỐI THỦ ---
Tên: {competitor_product.name}
Giá gốc: {competitor_product.original_price or 'Không có'}
Giá khuyến mãi: {competitor_product.discounted_price or 'Không có'}
Thông số:
{self._format_specs(competitor_product)}
Tính năng:
{self._format_features(competitor_product)}
"""
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text
        
    def _format_specs(self, product: Product) -> str:
        return "\n".join([f"- {s.name}: {s.value}" for s in product.specifications])
        
    def _format_features(self, product: Product) -> str:
        return "\n".join([f"- {f.description}" for f in product.features])
