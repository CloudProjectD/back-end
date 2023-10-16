from sqlalchemy.orm import Session
from app.models.domain import rooms
from app.models.schemas.rooms import Room


def create(db: Session, *, obj_in: rooms.RoomCreate, post_id: int) -> Room:
  db_obj = None
  if obj_in.starting_price:
    db_obj = Room(
      starting_price=obj_in.starting_price,
      price=obj_in.price,
      auction=obj_in.auction,
      deadline=obj_in.deadline,
      post_id=post_id,
    )
  else:
    db_obj = Room(
      price=obj_in.price,
      auction=obj_in.auction,
      deadline=obj_in.deadline,
      post_id=post_id,
    )
  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)
  return db_obj
