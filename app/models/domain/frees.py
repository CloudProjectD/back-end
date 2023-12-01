from typing import Optional
from pydantic import BaseModel
import datetime
from app.resources.status import Status
from typing import List


class FreeCreate(BaseModel):
    post_id: Optional[int] = None
    title: str
    content: str
    category: str
    status: Status


class FreeGet(BaseModel):
    post_id: Optional[int] = None
    title: str
    content: str
    status: Status
    category: str
    user_id: int
    created_at: datetime.datetime
    image_list: List[str]


class FreeUpdate(BaseModel):
    title: str
    content: str
    status: Status
    category: str
