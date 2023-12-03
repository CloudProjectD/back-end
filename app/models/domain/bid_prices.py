from pydantic import BaseModel


class BidPrice(BaseModel):
    bid_price: int
