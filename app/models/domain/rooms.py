from typing import Optional, List
from pydantic import BaseModel
import datetime
from app.resources.status import Status


class RoomCreate(BaseModel):
    post_id: Optional[int] = None
    price: int
    deposit: int
    title: str
    content: str
    category: str
    status: Status


class RoomGet(BaseModel):
    post_id: int
    deposit: int
    price: int
    title: str
    content: str
    status: Status
    category: str
    user_id: int
    created_at: datetime.datetime
    image_list: List[str]


class RoomUpdate(BaseModel):
    deposit: int
    price: int
    title: str
    content: str
    status: Status
    category: str
