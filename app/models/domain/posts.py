from pydantic import BaseModel
from typing import Optional
from app.resources.status import Status


class PostCreate(BaseModel):
    title: str
    content: str
    status: Status
    category: str
    user_id: Optional[int] = None
