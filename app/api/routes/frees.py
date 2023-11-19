import logging
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import frees
from app.crud import crud_frees, crud_posts

router = APIRouter()

@router.post("/create")
def create_free_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile],
    free_in: frees.FreeCreate = Depends()
) -> Any:
    # post data create
    post_data = crud_posts.create(db=db, obj_in=free_in, files=files)
    # free data create
    free_data = crud_frees.create(db=db, post_id=post_data.id)
    if free_data and post_data:
        return {"message": "free category create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
