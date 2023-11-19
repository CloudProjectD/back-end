import logging
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import rooms
from app.crud import crud_rooms, crud_posts

router = APIRouter()

@router.post("/create")
def create_room_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile],
    room_in: rooms.RoomCreate = Depends()
) -> Any:
    # post data create
    post_data = crud_posts.create(db=db, obj_in=room_in, files=files)
    # room data create
    room_date = crud_rooms.create(db=db, obj_in=room_in, post_id=post_data.id)
    if room_date and post_data:
        return {"message": "room category create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
