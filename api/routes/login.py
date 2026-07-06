from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from common.database import get_session
from common.models import User, UserReturn
from fastapi.security import OAuth2PasswordRequestForm
from common.auth import authenticate_user, create_access_token, authenticate_user, hash_password, get_user_from_db, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()

# Login endpoint
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: User = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": token, "token_type": "bearer"}

# Register new user endpoint
@router.post('/register', response_model=UserReturn)
async def register(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    user_with_name = await get_user_from_db(form_data.username)
    if user_with_name != None:
        raise HTTPException(status_code=409, detail="User with that name already exists")

    user = User(username=form_data.username, hashed_password=hash_password(form_data.password))
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserReturn(**user.model_dump())