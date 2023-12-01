from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import rooms
from app.crud import crud_rooms, crud_posts
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/create")
def create_room_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile] = None,
    room_in: rooms.RoomCreate = Depends()
) -> Any:
    # post data create
    post_data = crud_posts.create(db=db, obj_in=room_in, files=files)
    # room data create
    room_data = crud_rooms.create(db=db, obj_in=room_in, post_id=post_data.id)
    if room_data and post_data:
        return {"message": "room category create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )


@router.get("/get/{page}")
def get_room_posts(*, db: Session = Depends(database.get_db), page: int) -> Any:
    # room data get
    room_data = crud_posts.get(db=db, category="room", post_id=page)
    if room_data:
        res_data = jsonable_encoder(room_data)
        return JSONResponse(content=res_data)
    else:
        raise HTTPException(
            status_code=500,
            detail="getting room data failed",
        )


@router.get("/get_all")
def get_all_room_posts(*, db: Session = Depends(database.get_db)) -> Any:
    # room data get
    room_data = crud_posts.get_all(db=db, category="room")
    if room_data:
        res_data = jsonable_encoder(room_data)
        return JSONResponse(content=res_data)
    else:
        raise HTTPException(
            status_code=500,
            detail="getting all room data failed",
        )


@router.put("/update/{page}")
def update_room_posts(
    *,
    db: Session = Depends(database.get_db),
    page: int,
    room_in: rooms.RoomUpdate = Depends()
) -> Any:
    # market data update
    post_data = crud_posts.update(db=db, obj_in=room_in, post_id=page)
    room_data = crud_rooms.update(db=db, obj_in=room_in, post_id=page)
    if room_data and post_data:
        return {"message": "room category update success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="update failed",
        )


@router.delete("/delete/{page}")
def delete_market_posts(*, db: Session = Depends(database.get_db), page: int) -> Any:
    # market data delete
    try:
        crud_posts.delete(db=db, category="room", post_id=page)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="delete failed",
        )
    return {"message": "room category delete success"}
