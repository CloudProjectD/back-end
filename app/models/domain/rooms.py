from typing import Optional
from pydantic import BaseModel
import datetime
from app.resources.status import Status


class RoomCreate(BaseModel):
    post_id: Optional[int] = None
    starting_price: Optional[int] = None
    price: int
    auction: bool
    deadline: datetime.datetime
    title: str
    content: str
    status: Status
    category: str
    image: bool
