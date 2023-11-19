from sqlalchemy.orm import Session
from app.models.schemas.frees import Free


def create(db: Session, post_id: int) -> Free:
    db_obj = Free(
        post_id=post_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
