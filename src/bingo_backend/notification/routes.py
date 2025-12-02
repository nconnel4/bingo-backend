import asyncio
import json

from fastapi import APIRouter, Depends, Response

from bingo_backend.bingo.services import get_bingo_gif
from bingo_backend.database.core import get_session
from bingo_backend.notification.dtos import Notification
from bingo_backend.database.redis import redis
from sse_starlette.sse import EventSourceResponse


router = APIRouter()


async def notification_stream(session):
    async with redis.pubsub() as pubsub:
        await pubsub.subscribe("notifications")
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True)
            if message:
                data = json.loads(message["data"])
                if data.get("event") == "bingo":
                    gif = get_bingo_gif(session=session)
                    data["link"] = gif.link
                    data["description"] = gif.description
                yield json.dumps(data)
            await asyncio.sleep(1)

@router.post("/notifications")
async def create_notification(notification: Notification):
    await redis.publish("notifications", notification.model_dump_json())
    return Response(status_code=201)

@router.get("/notifications")
async def get_notifications(session = Depends(get_session)):
    return EventSourceResponse(notification_stream(session))
