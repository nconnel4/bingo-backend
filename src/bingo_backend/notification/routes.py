import json

from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect
from bingo_backend.bingo.services import get_bingo_gif
from bingo_backend.database.core import get_session

from bingo_backend.utils.websock_manager import manager

router = APIRouter()

@router.websocket("/notifications")
async def websocket_endpoint(websocket: WebSocket, session=Depends(get_session) ):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            if data["event"] == "bingo":
                gif = get_bingo_gif(session=session)
                data["link"] = gif.link
                data["description"] = gif.description
            await manager.broadcast(json.dumps(data))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.disconnect(websocket)