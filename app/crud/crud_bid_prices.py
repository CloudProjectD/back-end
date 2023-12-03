from sqlalchemy.orm import Session
from app.models.schemas.markets import Market


def bid(db: Session, *, post_id: int, bid_price: int) -> Market:
    market = db.query(Market).filter(Market.post_id == post_id).one()

    if bid_price > market.price:
        market.price = bid_price
        db.add(market)
        db.commit()
        db.refresh(market)
        return market

    return None
