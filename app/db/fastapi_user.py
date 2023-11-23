from typing import AsyncGenerator, List
from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    DeclarativeMeta,
    Mapped,
    relationship,
    declarative_base,
    sessionmaker,
)

from app.db.session import engine, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./temp.db"

Base: DeclarativeMeta = declarative_base()


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )

    class Config:
        from_attributes = True


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)
