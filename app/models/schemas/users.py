from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
