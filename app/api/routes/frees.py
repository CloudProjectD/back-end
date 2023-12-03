from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import frees
from app.crud import crud_frees, crud_posts
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.services.user_manager import current_active_user
from app.db.fastapi_user import User

router = APIRouter()


@router.post("/create")
def create_free_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile] = File(...),
    free_in: frees.FreeCreate,
    current_user: User = Depends(current_active_user)
) -> Any:
    # post data create
    post_data = crud_posts.create(db=db, obj_in=free_in, files=files, user=current_user)
    # free data create
    free_data = crud_frees.create(db=db, post_id=post_data.id)
    if free_data and post_data:
        return {"message": "free category create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )


@router.get("/get/{page}")
def get_free_posts(
    *,
    db: Session = Depends(database.get_db),
    page: int,
    current_user: User = Depends(current_active_user)
) -> Any:
    # free data get
    free_data = crud_posts.get(db=db, category="free", post_id=page, user=current_user)
    if free_data:
        res_data = jsonable_encoder(free_data)
        return JSONResponse(content=res_data)
    else:
        raise HTTPException(
            status_code=500,
            detail="getting free data failed",
        )


@router.get("/get_all")
def get_all_free_posts(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user)
) -> Any:
    # free data get
    free_data = crud_posts.get_all(db=db, category="free", user=current_user)
    if free_data:
        res_data = jsonable_encoder(free_data)
        return JSONResponse(content=res_data)
    else:
        raise HTTPException(
            status_code=500,
            detail="getting all free data failed",
        )


@router.put("/update/{page}")
def update_free_posts(
    *, db: Session = Depends(database.get_db), page: int, free_in: frees.FreeUpdate
) -> Any:
    # free data update
    post_data = crud_posts.update(db=db, obj_in=free_in, post_id=page)
    if post_data:
        return {"message": "free category update success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="update failed",
        )


@router.delete("/delete/{page}")
def delete_free_posts(*, db: Session = Depends(database.get_db), page: int) -> Any:
    # market data delete
    try:
        crud_posts.delete(db=db, category="free", post_id=page)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="delete failed",
        )
    return {"message": "free category delete success"}
