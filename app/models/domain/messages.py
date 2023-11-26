from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    post_id: int
    category: str
    sender_id: Optional[int] = None
    receipient_id: int
    content: str
    created_at: Optional[datetime] = None
