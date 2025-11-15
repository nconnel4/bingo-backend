from pydantic import BaseModel
from uuid import UUID

from bingo_backend.cardspace.dtos import CardSpaceRead


class CardBase(BaseModel):
    id: UUID
    user: str
    spaces: list[CardSpaceRead]

class CardRead(CardBase):
    pass