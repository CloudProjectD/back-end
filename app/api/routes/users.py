from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import database
from app.models.domain import users
from app.crud import crud_users
from app.services.user_manager import current_active_user
from app.db.fastapi_user import User
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post(path="/update", description="유저 정보를 업데이트합니다.(username, major 변경 가능)")
def register_user(
    *,
    db: Session = Depends(database.get_db),
    user: User = Depends(current_active_user),
    user_in: users.UpdateUser,
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


@router.get(path="/get/{user_id}", description="유저 id로 유저 정보를 가져옵니다.")
def get_user(
    *,
    db: Session = Depends(database.get_db),
    user_id: int,
) -> Any:
    user_data = crud_users.get_user_by_id(db=db, id=user_id)

    if user_data:
        enc_data = jsonable_encoder(user_data)
        return JSONResponse(content=enc_data)
    else:
        raise HTTPException(
            status_code=404,
            detail="find user by id failed",
        )


@router.get(path="/get_active", description="현재 활성화된 유저 정보를 가져옵니다.")
def get_current_active_user(
    *,
    db: Session = Depends(database.get_db),
    user: User = Depends(current_active_user),
) -> Any:
    user_data = crud_users.get_user_by_email(db=db, email=user.email)

    if user_data:
        enc_data = jsonable_encoder(user_data)
        return JSONResponse(content=enc_data)
    else:
        raise HTTPException(
            status_code=404,
            detail="find current active user failed",
        )
