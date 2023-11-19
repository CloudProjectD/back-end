from sqlalchemy.orm import Session
from app.models.domain import posts
from app.models.schemas.posts import Post
from app.services.aws import s3_upload
from fastapi import HTTPException
from fastapi import UploadFile
from typing import List
import datetime


def create(db: Session, *, obj_in: posts.PostCreate, files: List[UploadFile]) -> Post:
    db_obj = Post(
        title=obj_in.title,
        content=obj_in.content,
        status=obj_in.status,
        category=obj_in.category,
        created_at=datetime.datetime.today(),
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
