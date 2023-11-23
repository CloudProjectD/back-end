from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import database
from app.models.domain import users
from app.crud import crud_users
from app.services.user_manager import current_active_user
from app.db.fastapi_user import User


router = APIRouter()


@router.post(path="/update", description="유저 정보를 업데이트합니다.(username, major 변경 가능)")
def register_user(
    *,
    db: Session = Depends(database.get_db),
    user: User = Depends(current_active_user),
    user_in: users.UpdateUser
) -> Any:
    """
    Update user info
    (User can update username and major)
    """

    user_data = crud_users.update_user(db=db, email=user.email, obj_in=user_in)

    if user_data:
        return {"message": "Update user success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="Update user failed",
        )
