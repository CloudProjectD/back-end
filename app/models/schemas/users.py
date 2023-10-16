from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .posts import Post  # noqa: F401

class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    posts = relationship("Post", back_populates="user")
