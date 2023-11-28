from typing import Optional, List
from pydantic import BaseModel
import datetime
from app.resources.status import Status
from fastapi import UploadFile


class MarketCreate(BaseModel):
    post_id: Optional[int] = None
    starting_price: Optional[int] = None
    price: int
    auction: bool
    deadline: datetime.datetime
    title: str
    content: str
    status: Status
    category: str


class MarketGet(BaseModel):
    post_id: int
    starting_price: int
    price: int
    auction: bool
    deadline: datetime.datetime
    title: str
    content: str
    status: Status
    category: str
    user_id: int
    created_at: datetime.datetime
    image_list: List[str]


class MarketUpdate(BaseModel):
    starting_price: Optional[int] = None
    price: int
    auction: bool
    deadline: datetime.datetime
    title: str
    content: str
    status: Status
    category: str
