from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING
from app.resources.status import Status

if TYPE_CHECKING:
    from .users import User  # noqa: F401
    from .markets import Market  # noqa: F401


class Post(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), index=True)
    content = Column(String(255), index=True)
    user_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="posts")
    status = Column(Enum(Status), nullable=False, default=Status.PROCESSING)
    created_at = Column(DateTime, nullable=False)
    category = Column(String(255), index=True)
    image = Column(Boolean(), default=False)
    market = relationship("Market", back_populates="post")
    likes = relationship("Like", back_populates="post")
