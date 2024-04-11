from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user.models import User
from src.user.schemas import UserCreate


router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/add_user')
async def post_user(new_event: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(User).values(**new_event.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}