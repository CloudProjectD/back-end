from typing import Any
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import users
from app.models.schemas.users import User
router = APIRouter()

@router.post("/")
def create_user(
    *,
    db: Session = Depends(database.get_db),
    user_in: users.User
) -> Any:
    """
    Create new user.
    """
    user_in.username
    db_obj = User(email=user_in.email,username=user_in.username)
    print(User)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
