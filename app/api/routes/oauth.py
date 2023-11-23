from fastapi import APIRouter, Depends
from httpx_oauth.clients.google import GoogleOAuth2

from app.services.user_manager import current_active_user, fastapi_users
from app.db.fastapi_user import User
from app.core.config import settings
from app.services.google import auth_backend_google

router = APIRouter()

# auth/google/authorize
google_oauth_client = GoogleOAuth2(
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
)

# auth/google/callback
google_oauth_router = fastapi_users.get_oauth_router(
    oauth_client=google_oauth_client,
    backend=auth_backend_google,
    state_secret=settings.SECRET_KEY,
    redirect_url=settings.GOOGLE_CALLBACK_URL,
    associate_by_email=True,
)

router.include_router(google_oauth_router, prefix="/google")


@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
