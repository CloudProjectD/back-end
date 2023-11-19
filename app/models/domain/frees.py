from typing import Optional
from pydantic import BaseModel
import datetime
from app.resources.status import Status


class FreeCreate(BaseModel):
    post_id: Optional[int] = None
    title: str
    content: str
    category: str
    status: Status
