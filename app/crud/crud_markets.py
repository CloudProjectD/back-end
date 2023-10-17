from sqlalchemy.orm import Session
from app.models.domain import markets
from app.models.schemas.markets import Market


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
