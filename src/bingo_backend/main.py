from functools import lru_cache

from fastapi import FastAPI
from bingo_backend.config import Settings

@lru_cache
def get_settings():
    return Settings()

from bingo_backend.database.core import engine, Base
from bingo_backend.api import router
from bingo_backend.card.models import *
from bingo_backend.cardspace.models import *
from bingo_backend.space.models import *


app = FastAPI()


app.include_router(router)
