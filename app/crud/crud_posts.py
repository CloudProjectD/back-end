from sqlalchemy.orm import Session
from app.models.domain import posts
from app.models.schemas.posts import Post
from app.services.aws import s3_upload, s3_get
from fastapi import HTTPException
from fastapi import UploadFile
from typing import List, Any
import datetime
from app.crud.crud_markets import get as get_market, delete as market_delete
from app.crud.crud_frees import get as get_free, delete as free_delete
from app.crud.crud_rooms import get as get_room, delete as room_delete
from app.crud.crud_users import get_user_by_email
from app.db.fastapi_user import User


def create(
    db: Session, *, obj_in: posts.PostCreate, files: List[UploadFile], user: User
) -> Post:
    db_obj = Post(
        title=obj_in.title,
        content=obj_in.content,
        status=obj_in.status,
        category=obj_in.category,
        created_at=datetime.datetime.today(),
        user_id=get_user_by_email(
            db=db, email=user.email
        ).id,
    )
    # image bool value insert
    db_obj.image = True if files else False
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    # if image exits, do uploading in s3
    if files:
        s3_result = s3_upload(
            files=files,
            post_id=db_obj.id,
            user_email=user.email,
            category=obj_in.category,
        )
        if not s3_result:
            raise HTTPException(
                status_code=500,
                detail="s3 upload failed",
            )
    return db_obj


def get(db: Session, *, category: str, post_id: int, user: User) -> Any | None:
    post_data = (
        db.query(Post).filter(Post.id == post_id, Post.category == category).one()
    )
    if category == "market":
        file_list = []
        if post_data.image:
            file_list = s3_get(
                post_id=post_data.id,
                user_email=user.email,
                category=category,
            )
        result = get_market(
            db, post_id=post_id, post_data=post_data, file_list=file_list
        )
        return result
    elif category == "free":
        file_list = []
        if post_data.image:
            file_list = s3_get(
                post_id=post_data.id,
                user_email=user.email,
                category=category,
            )
        result = get_free(db, post_id=post_id, post_data=post_data, file_list=file_list)
        return result
    elif category == "room":
        file_list = []
        if post_data.image:
            file_list = s3_get(
                post_id=post_data.id,
                user_email=user.email,
                category=category,
            )
        result = get_room(db, post_id=post_id, post_data=post_data, file_list=file_list)
        return result
    else:
        return None


def get_all(db: Session, category: str, user: User) -> list[Any]:
    post_data = db.query(Post).filter(Post.category == category).all()
    result = []
    if category == "market":
        for post in post_data:
            file_list = []
            if post.image:
                file_list = s3_get(
                    post_id=post.id,
                    user_email=user.email,  # should be changed with user email
                    category=category,
                )
            market_data = get_market(
                db, post_id=post.id, post_data=post, file_list=file_list
            )
            result.append(market_data)
    elif category == "free":
        for post in post_data:
            file_list = []
            if post.image:
                file_list = s3_get(
                    post_id=post.id,
                    user_email=user.email,  # should be changed with user email
                    category=category,
                )
            free_data = get_free(
                db, post_id=post.id, post_data=post, file_list=file_list
            )
            result.append(free_data)
    elif category == "room":
        for post in post_data:
            file_list = []
            if post.image:
                file_list = s3_get(
                    post_id=post.id,
                    user_email=user.email,  # should be changed with user email
                    category=category,
                )
            room_data = get_room(
                db, post_id=post.id, post_data=post, file_list=file_list
            )
            result.append(room_data)
    return result


def update(db: Session, *, obj_in: posts.PostUpdate, post_id: int) -> Post:
    db_obj = (
        db.query(Post)
        .filter(Post.id == post_id, Post.category == obj_in.category)
        .one()
    )
    db_obj.title = obj_in.title
    db_obj.content = obj_in.content
    db_obj.status = obj_in.status
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete(db: Session, *, category: str, post_id: int):
    db_obj = db.query(Post).filter(Post.id == post_id, Post.category == category).one()
    if category == "market":
        market_delete(db=db, post_id=post_id)
    elif category == "free":
        free_delete(db=db, post_id=post_id)
    elif category == "room":
        room_delete(db=db, post_id=post_id)
    db.delete(db_obj)
    db.commit()
