from pydantic import BaseModel
from typing import Optional


class LikePostResponse(BaseModel):
    representative_image: Optional[str] = None
    title: str
    seller: int
    category: str

    # SQLAlchemy ORM model instance -> Pydantic model instance
    class Config:
        orm_mode = True
