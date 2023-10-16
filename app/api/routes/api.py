from fastapi import APIRouter

from app.api.routes import users
from app.api.routes import rooms


router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(rooms.router, tags=["rooms"])
