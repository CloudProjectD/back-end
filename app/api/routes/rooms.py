import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import rooms
from app.crud import crud_rooms, crud_posts

router = APIRouter()


@router.post("/create/room")
def create_room_posts(
    *, db: Session = Depends(database.get_db), room_in: rooms.RoomCreate
) -> Any:
    """
    Create new user.
    """
    # post data create
    post_data = crud_posts.create(db=db, obj_in=room_in)
    print(post_data)
    # room data create
    room_data = crud_rooms.create(db=db, obj_in=room_in, post_id=post_data.id)
    print(room_data)
    if room_data and post_data:
        return {"message": "create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
