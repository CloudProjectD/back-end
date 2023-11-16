from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User  # noqa: F401
    from .posts import Post  # noqa: F401

class Like(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")
