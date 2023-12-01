from sqlalchemy.orm import Session
from app.models.domain import posts
from app.models.schemas.posts import Post
from app.services.aws import s3_upload, s3_get
from fastapi import HTTPException
from fastapi import UploadFile
from typing import List, Any
import datetime
from app.models.domain import markets
from app.crud.crud_markets import get as get_market, delete as market_delete
from app.crud.crud_frees import get as get_free, delete as free_delete


def create(db: Session, *, obj_in: posts.PostCreate, files: List[UploadFile]) -> Post:
    db_obj = Post(
        title=obj_in.title,
        content=obj_in.content,
        status=obj_in.status,
        category=obj_in.category,
        created_at=datetime.datetime.today(),
        user_id=1,  # should be changed with user email
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
            user_email="sumink0903@gmail.com",
            category=obj_in.category,
        )
        if not s3_result:
            raise HTTPException(
                status_code=500,
                detail="s3 upload failed",
            )
    return db_obj


def get(db: Session, *, category: str, post_id: int) -> Any | None:
    post_data = (
        db.query(Post).filter(Post.id == post_id, Post.category == category).one()
    )
    if category == "market":
        file_list = []
        if post_data.image:
            file_list = s3_get(
                post_id=post_data.id,
                user_email="sumink0903@gmail.com",
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
                user_email="sumink0903@gmail.com",
                category=category,
            )
        result = get_free(db, post_id=post_id, post_data=post_data, file_list=file_list)
        return result
    else:
        return None


def get_all(db: Session, category: str) -> list[Any]:
    post_data = db.query(Post).filter(Post.category == category).all()
    result = []
    if category == "market":
        for post in post_data:
            file_list = []
            if post.image:
                file_list = s3_get(
                    post_id=post.id,
                    user_email="sumink0903@gmail.com",  # should be changed with user email
                    category=category,
                )
            market_data = get_market(
                db, post_id=post.id, post_data=post, file_list=file_list
            )
            result.append(market_data)
    if category == "free":
        for post in post_data:
            file_list = []
            if post.image:
                file_list = s3_get(
                    post_id=post.id,
                    user_email="sumink0903@gmail.com",  # should be changed with user email
                    category=category,
                )
            free_data = get_free(
                db, post_id=post.id, post_data=post, file_list=file_list
            )
            result.append(free_data)
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
    db.delete(db_obj)
    db.commit()
