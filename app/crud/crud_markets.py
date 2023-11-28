from sqlalchemy.orm import Session
from app.models.domain import markets
from app.models.schemas.markets import Market
from app.models.schemas.posts import Post
from typing import Any, List


def create(db: Session, *, obj_in: markets.MarketCreate, post_id: int) -> Market:
    db_obj = None
    if obj_in.starting_price:
        db_obj = Market(
            starting_price=obj_in.starting_price,
            price=obj_in.price,
            auction=obj_in.auction,
            deadline=obj_in.deadline,
            post_id=post_id,
        )
    else:
        db_obj = Market(
            price=obj_in.price,
            auction=obj_in.auction,
            deadline=obj_in.deadline,
            post_id=post_id,
        )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get(db: Session, *, post_id: int, post_data: Post, file_list: List[str]) -> Any:
    market_data = db.query(Market).filter(Market.post_id == post_id).one()
    result = markets.MarketGet(
        post_id=post_id,
        starting_price=market_data.starting_price,
        price=market_data.price,
        auction=market_data.auction,
        deadline=market_data.deadline,
        title=post_data.title,
        content=post_data.content,
        status=post_data.status,
        category=post_data.category,
        user_id=post_data.user_id,
        created_at=post_data.created_at,
        image_list=file_list,
    )
    return result


def update(db: Session, *, obj_in: markets.MarketUpdate, post_id: int) -> Market:
    db_obj = db.query(Market).filter(Market.post_id == post_id).one()
    db_obj.starting_price = obj_in.starting_price
    db_obj.price = obj_in.price
    db_obj.auction = obj_in.auction
    db_obj.deadline = obj_in.deadline
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
