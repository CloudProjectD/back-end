from typing import Optional
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
