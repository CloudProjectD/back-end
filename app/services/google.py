from typing import Any, Optional
import requests
import json
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy import Strategy

from app.services.user_manager import bearer_transport, get_jwt_strategy
from app.db.fastapi_user import User
from app.db.session import SessionLocal
from app.crud.crud_users import create_user, get_user_by_email


class GoogleAuthBackend(AuthenticationBackend):
    async def login(self, strategy: Strategy, user: User) -> Any:
        strategy_response = await super().login(strategy, user)
        member = True
        for account in user.oauth_accounts:
            usermail = account.account_email

            if usermail.split("@")[1] != "khu.ac.kr":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="경희대 학교 메일로만 가입 가능합니다.",
                )

            db = SessionLocal()
            try:
                user = get_user_by_email(db=db, email=usermail)
                if not user:
                    create_user(db=db, email=usermail)
                    member = False
            finally:
                db.close()

        return JSONResponse(
            content={"info": json.loads(strategy_response.body), "member": member}
        )

    def get_google_access_token(self, user: User) -> Optional[str]:
        for account in user.oauth_accounts:
            if account.oauth_name == "google":
                return account.access_token
        return None


def get_profile_from_google(access_token: str) -> dict:
    response = requests.get(
        url="https://www.googleapis.com/oauth2/v3/userinfo",
        params={"access_token": access_token},
    )
    if not response.ok:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to get user information from Google.",
        )
    return response.json()


auth_backend_google = GoogleAuthBackend(
    name="jwt-google",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
