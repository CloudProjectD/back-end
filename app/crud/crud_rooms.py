from sqlalchemy.orm import Session
from app.models.domain import rooms
from app.models.schemas.rooms import Room


def create(db: Session, *, obj_in: rooms.RoomCreate, post_id: int) -> Room:
    db_obj = Room(
      price=obj_in.price,
      post_id=post_id,
      deposit=obj_in.deposit,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
