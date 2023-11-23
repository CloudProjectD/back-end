from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: Optional[str]
    email: str
    major: Optional[str]


class UpdateUser(BaseModel):
    username: str
    major: str
