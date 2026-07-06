from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pwdlib import PasswordHash
from common.settings import settings
from common.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from common.database import engine
from sqlalchemy import select


ACCESS_TOKEN_EXPIRE_MINUTES = 1
AUTH_ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
password_hash = PasswordHash.recommended()

#hash password from plaintext
def hash_password(password: str) -> str:
    return password_hash.hash(password)

#verify plaintex password by hashing it and comparing to the hashed password we've stored
def verify_password(plain: str, hashed: str) -> str:
    return password_hash.verify(plain, hashed)

#create a JWT token with some data in dictionary form as it's payload
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({ 'exp' : expire })
    return jwt.encode(to_encode, settings.AUTH_SECRET_KEY, algorithm=AUTH_ALGORITHM)

#Get the user with the specified username from the db if they exist
async def get_user_from_db(username: str):
    async with AsyncSession(bind=engine) as session:
        results = await session.execute(select(User).where(User.username == username))
        try:
            return results.scalars().one()
        except:
            return None

# get the current user based on the contents of a JWT token
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, settings.AUTH_SECRET_KEY, algorithms=[AUTH_ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Invalid Token')
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid Token')
    user = await get_user_from_db(username)
    if user is None:
        raise HTTPException(status_code=401, detail='User not found')
    return user
    
# check the database to see if there's a user with the same username 
# and hashed password matching the hash of the plaintext password
# if there is, return that user
async def authenticate_user(username: str, password_plaintext: str) -> User:
    print('authenticate_user - running...')
    user: User = await get_user_from_db(username)
    if user:
        print('authenticate_user - got user in db!')
        if verify_password(password_plaintext, user.hashed_password):
            return user
        else:
            print('authenticate_user - password does not match!')
    else:
        print('authenticate_user - user is not in the db!')
    return None
