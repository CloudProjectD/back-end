from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from app.models.domain import messages
from app.services.aws import DynamoDBHandler
import datetime
from app.services.user_manager import current_active_user
from app.db.fastapi_user import User
from app.crud.crud_users import get_user_by_email

router = APIRouter()

@router.post("/create")
def create_message(
    *,
    message_in: messages.Message = Depends(),
    current_user: User = Depends(current_active_user)
) -> Any:
    message_data = {
        "post_id": message_in.post_id,
        "category": message_in.category,
        "sender_id": get_user_by_email(current_user.email).id,
        "receipient_id": message_in.receipient_id,
        "content": message_in.content,
        "created_at": datetime.datetime.today(),
    }

    if not DynamoDBHandler.put_object(messages.Message(**message_data)):
        raise HTTPException(
            status_code=500,
            detail="create failed",
        )
    else: 
        return {"message": "Send post message success"}


