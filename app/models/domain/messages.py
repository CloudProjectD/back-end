from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class Message(BaseModel):
    id: str = str(uuid.uuid4())
    post_id: int
    category: str
    sender: Optional[int] = None
    recipient: int
    content: str
    created_at: datetime = datetime.today()


class MessageInput(BaseModel):
    post_id: int
    category: str
    recipient: int
    content: str
