from sqlalchemy.orm import Session
from typing import List
from app.models.schemas.likes import Like
from app.models.schemas.posts import Post
from app.services.aws import s3_get
from app.models.domain.likes import LikePostResponse
from fastapi import HTTPException


def get_liked_post_by_user(db: Session, *, user_id: int) -> List[LikePostResponse]:
    likes = db.query(Like).filter(Like.user_id == user_id).all()
    print(likes)
    liked_posts = [
        LikePostResponse(
            title=like.posts.title,
            representative_image=get_first_image_of_post(
                like.posts.id, user_id, like.posts.category
            ),
            seller=like.posts.user_id,
            category=like.posts.category,
        )
        for like in likes
    ]

    return liked_posts


def get_first_image_of_post(post_id: int, user_id: int, post_category: str):
    file_list = s3_get(
        post_id=post_id,
        user_email=user_id,
        category=post_category,
    )
    if file_list:
        return file_list[0]
    else:
        return None


def create_like(db: Session, *, post_id: int, user_id: int) -> Like:
    # Check if the post exists
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Create the like
    like = Like(post_id=post_id, user_id=user_id)
    db.add(like)
    db.commit()
    db.refresh(like)

    return like


def delete_like(db: Session, *, post_id: int, user_id: int) -> Like:
    # Check if the like exists
    like = (
        db.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
    )
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")

    # Delete the like
    db.delete(like)
    db.commit()

    return like
