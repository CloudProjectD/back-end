from pydantic import BaseModel, Field
from datetime import datetime

class Message(BaseModel):
    post_id: int
    category: str
    sender_id: int
    receipient_id: int
    content: str
    created_at: datetime
