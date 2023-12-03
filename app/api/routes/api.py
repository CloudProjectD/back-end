from fastapi import APIRouter

from app.api.routes import users
from app.api.routes import markets
from app.api.routes import rooms
from app.api.routes import frees
from app.api.routes import oauth
from app.api.routes import messages
from app.api.routes import likes
from app.api.routes import reports
from app.api.routes import bid_prices

router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(markets.router, tags=["markets"], prefix="/market")
router.include_router(rooms.router, tags=["rooms"], prefix="/room")
router.include_router(frees.router, tags=["frees"], prefix="/free")
router.include_router(oauth.router, tags=["auth"], prefix="/auth")
router.include_router(messages.router, tags=["messages"], prefix="/message")
router.include_router(likes.router, tags=["likes"], prefix="/like")
router.include_router(reports.router, tags=["reports"], prefix="/report")
router.include_router(bid_prices.router, tags=["bid_prices"], prefix="/bid")
