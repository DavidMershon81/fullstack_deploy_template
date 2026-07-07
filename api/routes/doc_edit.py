from pycrdt import Doc, Text
from pycrdt.websocket import WebsocketServer
from pycrdt.websocket.asgi_server import ASGIServer
from fastapi import APIRouter, WebSocket
#from sqlmodel import SQLModel
import asyncio

router = APIRouter()

doc = Doc()
doc["text"] = text = Text()

websocket_server = WebsocketServer()
websocket_server.rooms['test_room'] = doc

@router.websocket('/doc/ws/test_room')
async def doc_ws(websocket: WebSocket):
    await websocket.accept()
    await websocket_server.start() 
    await websocket_server.serve(websocket)
