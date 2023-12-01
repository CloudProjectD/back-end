from sqlalchemy.orm import Session
from app.models.schemas.likes import Like
from app.models.schemas.posts import Post
from fastapi import HTTPException


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
