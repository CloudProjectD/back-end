import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import markets
from app.crud import crud_markets, crud_posts

router = APIRouter()


@router.post("/create")
def create_market_posts(
    *, db: Session = Depends(database.get_db), market_in: markets.MarketCreate
) -> Any:
    """
    Create new user.
    """
    # post data create
    post_data = crud_posts.create(db=db, obj_in=market_in)
    # room data create
    market_data = crud_markets.create(db=db, obj_in=market_in, post_id=post_data.id)
    if market_data and post_data:
        return {"message": "create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
