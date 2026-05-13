import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Cấu hình kết nối PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sales_agent:secretpassword@localhost:15432/sales_agent_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Tạo tất cả các bảng trong DB nếu chưa có"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Generator cung cấp session DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
