from fastapi import APIRouter
from datetime import datetime
from common.settings import settings

router = APIRouter()

@router.get('/health')
async def get_health():
    return { 'health' : 'ok', 'time' : datetime.now() }

@router.get('/test_env_vars')
async def get_test_env_vars():
    return { 'settings.TEST_ENV_VAR' : settings.TEST_ENV_VAR }

