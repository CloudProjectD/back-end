import logging
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import markets
from app.crud import crud_markets, crud_posts

router = APIRouter()


@router.post("/create")
def create_market_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile],
    market_in: markets.MarketCreate = Depends()
) -> Any:
    """
    Create new user.
    """
    # post data create
    post_data = crud_posts.create(db=db, obj_in=market_in, files=files)
    # room data create
    market_data = crud_markets.create(db=db, obj_in=market_in, post_id=post_data.id)
    if market_data and post_data:
        return {"message": "create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
