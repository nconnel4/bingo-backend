from pydantic import BaseModel, computed_field, Field
from uuid import UUID

from bingo_backend.space.dtos import SpaceRead


class CardSpaceBase(BaseModel):
    id: UUID
    position: int
    is_complete: bool

class CardSpaceRead(CardSpaceBase):
    space: SpaceRead = Field(exclude=True)

    @computed_field
    def text(self) -> str:
        return self.space.text
