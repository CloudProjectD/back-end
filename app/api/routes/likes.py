from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.aws import s3_get
from app.api.dependencies import database
from app.crud.crud_likes import create_like, delete_like, get_liked_post_by_user
from app.models.domain.likes import LikePostResponse
from app.services.user_manager import current_active_user
from app.crud.crud_users import get_user_by_email
from app.db.fastapi_user import User


router = APIRouter()


@router.get(
    "/list",
    response_model=List[LikePostResponse],
    description="사용자가 관심 표시한 물품의 리스트를 반환합니다.",
)
def get_liked_posts(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
) -> Any:
    current_user_id = get_user_by_email(db=db, email=current_user.email).id

    liked_posts = get_liked_post_by_user(db=db, user_id=current_user_id)

    if liked_posts:
        return liked_posts
    else:
        raise HTTPException(
            status_code=404,
            detail="No liked post found for this user",
        )


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
            status_code=500,
            detail="like create failed",
        )


@router.delete("/post/{post_id}", description="게시글에 관심 표시를 취소합니다.")
def unlike_post(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
    post_id: int,
) -> Any:
    current_user_id = get_user_by_email(db=db, email=current_user.email).id

    deleted_like = delete_like(db=db, post_id=post_id, user_id=current_user_id)

    if deleted_like:
        return {"message": "Like deleted successfully"}
    else:
        raise HTTPException(
            status_code=500,
            detail="like delete failed",
        )
