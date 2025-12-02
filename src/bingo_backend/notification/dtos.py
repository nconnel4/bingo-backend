import uuid

from pydantic import BaseModel

class Notification(BaseModel):
    event: str
    message: str

class NotificationMessage(Notification):
    id: str = uuid.uuid4()
    link: str | None = None