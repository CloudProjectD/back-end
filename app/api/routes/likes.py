from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import database
from app.crud.crud_likes import create_like
from app.models.domain import users
from app.services.user_manager import current_active_user
from app.crud.crud_users import get_user_by_email
from app.db.fastapi_user import User


router = APIRouter()


@router.post("/post/{post_id}", description="게시글에 관심 표시를 합니다.")
def like_post(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
    post_id: int,
) -> Any:
    current_user_id = get_user_by_email(db=db, email=current_user.email).id

    like = create_like(db=db, post_id=post_id, user_id=current_user_id)

    if like:
        return {"message": "Like added succcessfully"}
    else:
        raise HTTPException(
            status_cod=500,
            detail="like create failed",
        )
