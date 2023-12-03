from sqlalchemy.orm import Session
from app.models.domain import rooms
from app.models.schemas.rooms import Room
from app.models.schemas.posts import Post
from typing import Any, List


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


def get(db: Session, *, post_id: int, post_data: Post, file_list: List[str]) -> Any:
    room_data = db.query(Room).filter(Room.post_id == post_id).one()
    result = rooms.RoomGet(
        post_id=post_id,
        deposit=room_data.deposit,
        price=room_data.price,
        title=post_data.title,
        content=post_data.content,
        status=post_data.status,
        category=post_data.category,
        user_id=post_data.user_id,
        created_at=post_data.created_at,
        image_list=file_list,
    )
    return result


def update(db: Session, *, obj_in: rooms.RoomUpdate, post_id: int) -> Room:
    db_obj = db.query(Room).filter(Room.post_id == post_id).one()
    db_obj.deposit = obj_in.deposit
    db_obj.price = obj_in.price
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete(db: Session, *, post_id: int):
    db_obj = db.query(Room).filter(Room.post_id == post_id).one()
    db.delete(db_obj)
    db.commit()
