from fastapi import  Depends, APIRouter
from common.models import User, UserReturn
from common.auth import get_current_user

router = APIRouter(prefix="/users")

# Protected endpoint that returns the current user's data
@router.get("/me", response_model=UserReturn)
async def read_me(user: User = Depends(get_current_user)):
    return UserReturn(**user.model_dump())