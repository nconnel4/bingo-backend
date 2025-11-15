from pydantic import BaseModel

class SpaceBase(BaseModel):
    id: int
    text: str

class SpaceRead(SpaceBase):
    pass