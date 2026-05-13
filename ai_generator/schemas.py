from pydantic import BaseModel, Field

class SpecificationItem(BaseModel):
    name: str = Field(description="Tên thông số (ví dụ: RAM, ROM, Chipset, Camera, v.v.)")
    value: str = Field(description="Giá trị của thông số (ví dụ: 8GB, 128GB, 50MP, v.v.)")

class ProductData(BaseModel):
    product_name: str = Field(description="Tên đầy đủ của sản phẩm")
    original_price: int | None = Field(default=None, description="Giá niêm yết/giá gốc của sản phẩm (số nguyên), ví dụ: 5190000. Nếu không thấy thì để null.")
    discounted_price: int | None = Field(default=None, description="Giá khuyến mãi của sản phẩm (số nguyên). Nếu không có trả về null.")
    specifications: list[SpecificationItem] = Field(
        description="Danh sách các thông số kỹ thuật chi tiết của sản phẩm"
    )
    key_features: list[str] = Field(
        description="Danh sách các tính năng hoặc điểm nổi bật chính của sản phẩm"
    )
