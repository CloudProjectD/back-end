from sqlalchemy.orm import Session
from app.models.domain import posts
from app.models.schemas.posts import Post
import datetime

def create(db: Session, *, obj_in: posts.PostCreate) -> Post:
  db_obj = Post(
    title=obj_in.title,
    content=obj_in.content,
    status=obj_in.status,
    category=obj_in.category,
    image=obj_in.image,
    created_at=datetime.datetime.today()
  )
  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)
  return db_obj
