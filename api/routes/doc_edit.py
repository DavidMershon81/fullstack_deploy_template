from pycrdt import Doc, Text
from pycrdt.websocket import WebsocketServer
from fastapi import APIRouter, WebSocket

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
