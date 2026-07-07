from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.settings import settings
from routes.main import api_router
from common.sanity_checks import print_settings_test_var

print_settings_test_var()

app = FastAPI()

origins = [ settings.FRONTEND_URL_DEV ] if settings.IS_DEV else [ settings.FRONTEND_URL_PROD ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
