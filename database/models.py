from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    original_price = Column(Integer, nullable=True)
    discounted_price = Column(Integer, nullable=True)
    url = Column(String, nullable=True)
    
    specifications = relationship("Specification", back_populates="product", cascade="all, delete-orphan")
    features = relationship("Feature", back_populates="product", cascade="all, delete-orphan")

class Specification(Base):
    __tablename__ = 'specifications'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    name = Column(String, nullable=False)
    value = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="specifications")

class Feature(Base):
    __tablename__ = 'features'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    description = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="features")
