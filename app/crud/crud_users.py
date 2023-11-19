from sqlalchemy.orm import Session
from app.models.domain import users
from app.models.schemas.users import User


def create_user(db: Session, email: str) -> User:
    db_obj = User(
        email=email,
        username=None,
        major=None,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user


def update_user(db: Session, *, email: str, obj_in: users.UpdateUser) -> User:
    user = get_user_by_email(db, email)

    if user:
        user.username = obj_in.username
        user.major = obj_in.major

        db.commit()
        db.refresh(user)

        return user

    return None
