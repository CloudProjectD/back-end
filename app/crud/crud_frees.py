from sqlalchemy.orm import Session
from app.models.schemas.frees import Free
from app.models.schemas.posts import Post
from app.models.domain import frees
from typing import Any, List


def create(db: Session, post_id: int) -> Free:
    db_obj = Free(
        post_id=post_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get(db: Session, *, post_id: int, post_data: Post, file_list: List[str]) -> Any:
    result = frees.FreeGet(
        post_id=post_id,
        title=post_data.title,
        content=post_data.content,
        status=post_data.status,
        category=post_data.category,
        user_id=post_data.user_id,
        created_at=post_data.created_at,
        image_list=file_list,
    )
    return result


def delete(db: Session, *, post_id: int):
    db_obj = db.query(Free).filter(Free.post_id == post_id).one()
    db.delete(db_obj)
    db.commit()
