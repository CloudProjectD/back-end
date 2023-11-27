import logging
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.models.domain import markets
from app.crud import crud_markets, crud_posts
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/create")
def create_market_posts(
    *,
    db: Session = Depends(database.get_db),
    files: List[UploadFile],
    market_in: markets.MarketCreate = Depends()
) -> Any:
    # post data create
    post_data = crud_posts.create(db=db, obj_in=market_in, files=files)
    # market data create
    market_data = crud_markets.create(db=db, obj_in=market_in, post_id=post_data.id)
    if market_data and post_data:
        return {"message": "market category create success"}
    else:
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )


@router.get("/get/{category}/{page}")
def get_market_posts(
    *, db: Session = Depends(database.get_db), category: str, page: int
) -> tuple[Any, list[UploadFile] | list[Any]]:
    # market data get
    market_data = crud_posts.get(db=db, category=category, post_id=page)
    if market_data:
        res_data = jsonable_encoder(market_data)
        return JSONResponse(content=res_data)
    else:
        raise HTTPException(
            status_code=500,
            detail="getting market data failed",
        )
