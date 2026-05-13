from sqlalchemy.orm import Session
from .models import Product, Specification, Feature
from ai_generator.schemas import ProductData

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_product_data(self, data: ProductData, url: str = None) -> Product:
        # Tạo đối tượng Product
        product = Product(
            name=data.product_name,
            original_price=data.original_price,
            discounted_price=data.discounted_price,
            url=url
        )
        self.db.add(product)
        self.db.flush() # Lấy ID của product
        
        # Thêm Specifications
        for spec in data.specifications:
            db_spec = Specification(product_id=product.id, name=spec.name, value=spec.value)
            self.db.add(db_spec)
            
        # Thêm Features
        for feature in data.key_features:
            db_feature = Feature(product_id=product.id, description=feature)
            self.db.add(db_feature)
            
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all_products(self):
        return self.db.query(Product).all()
