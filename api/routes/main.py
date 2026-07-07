from fastapi import APIRouter

from routes import login, companies, users, misc, doc_edit

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(companies.router)
api_router.include_router(users.router)
api_router.include_router(misc.router)
api_router.include_router(doc_edit.router)