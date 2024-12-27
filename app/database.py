# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # 모델에서 Base import

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 테이블 생성
def create_tables():
    print("테이블 생성 중...")
    Base.metadata.create_all(bind=engine)
    print("테이블이 성공적으로 생성되었습니다.")


# 테이블 생성 함수 호출
create_tables()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
