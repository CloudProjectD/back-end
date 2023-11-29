from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from app.models.domain import messages
from app.services.aws import DynamoDBHandler
import datetime
import uuid
from app.services.user_manager import current_active_user
from app.db.fastapi_user import User
from app.crud import crud_posts
from app.crud.crud_users import get_user_by_email
from sqlalchemy.orm import Session
from app.api.dependencies import database

router = APIRouter()


@router.post("/create")
def create_message(
    *,
    db: Session = Depends(database.get_db),
    message_in: messages.MessageInput,
    current_user: User = Depends(current_active_user)
) -> Any:
    current_user_id = get_user_by_email(db=db, email=current_user.email).id
    message_data = {
        "id": str(uuid.uuid4()),
        "post_id": message_in.post_id,
        "category": message_in.category,
        "sender": current_user_id,
        "recipient": message_in.recipient,
        "content": message_in.content,
        "created_at": datetime.datetime.today(),
    }

    dynamodb_handler = DynamoDBHandler()

    if not dynamodb_handler.put_object(message=messages.Message(**message_data)):
        raise HTTPException(
            status_code=500,
            detail="create message failed",
        )
    else:
        return {"message": "Send post message success"}


#유저와 관련된 전체 메시지 반환
@router.get("/list")
def get_user_messages(
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
) -> Any:
    dynamodb_handler = DynamoDBHandler()

    current_user_id = get_user_by_email(db=db, email=current_user.email).id
    all_user_messages = dynamodb_handler.get_all_user_objects(user_id=current_user_id)
    if not all_user_messages:
        raise HTTPException(
            status_code=404,
            detail="user messages not found"
        )
    
    result = []
    for msg in all_user_messages:
        print(msg["category"], msg["post_id"])
        post_info = crud_posts.get(db=db, category=msg["category"], post_id=int(msg["post_id"]))
        print(post_info)
        if post_info:
            result.append({
                "message": msg, 
                "post": post_info,
            })
    
    
    return result


# post_id에 해당하는 user의 메시지 가져오기
@router.get("/list/{post_id}")
def get_post_messages(
    post_id: int,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(current_active_user),
) -> Any:
    dynamodb_handler = DynamoDBHandler()

    current_user_id = get_user_by_email(db=db, email=current_user.email).id
    all_user_post_messages = dynamodb_handler.get_user_post_objects(user_id=current_user_id, post_id=post_id)
    if not all_user_post_messages:
        raise HTTPException(
            status_code=404,
            detail="post messages not found"
        )

    return all_user_post_messages