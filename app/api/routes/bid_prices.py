from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import database
from app.crud.crud_bid_prices import bid
from app.models.domain.bid_prices import BidPrice
from app.services.user_manager import current_active_user
from app.crud.crud_users import get_user_by_email
from app.db.fastapi_user import User

router = APIRouter()


@router.put("/{post_id}", description="경매 게시글의 경매 가격을 제시합니다.")
def bid_for_item(
    *,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
    post_id: int,
    bid_price: BidPrice,
) -> Any:
    current_user_name = get_user_by_email(db=db, email=current_user.email).username

    # market price update
    market = bid(db=db, post_id=post_id, bid_price=bid_price.bid_price)
    if market:
        return {"message": f"{current_user_name} successfully placed a bid"}
    else:
        raise HTTPException(
            status_code=400,
            detail="Bid price must be higher than current price",
        )
