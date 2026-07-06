from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from common.settings import settings

#Everything below is what's needed to set up the async db engine
#so we can use it with dependency injection in the endpoints

DATABASE_URL = settings.DB_URL_DEV if settings.IS_DEV else settings.DB_URL_PROD
engine = create_async_engine(f"postgresql+asyncpg://{DATABASE_URL}", echo=settings.IS_DEV)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
