from fastapi import APIRouter

from app.api.routes import users
from app.api.routes import markets
from app.api.routes import oauth

router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(markets.router, tags=["markets"], prefix="/market")
router.include_router(oauth.router, tags=["auth"], prefix="/auth")
