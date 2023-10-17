from sqlalchemy import Boolean, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
from app.db.base_class import Base

if TYPE_CHECKING:
    from .posts import Post  # noqa: F401


class Market(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    starting_price = Column(Integer)
    price = Column(Integer, nullable=False)
    auction = Column(Boolean(), default=False)
    deadline = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="market")
