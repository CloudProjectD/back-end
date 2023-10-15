from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import HOST
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:1234@{HOST}:3306/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
