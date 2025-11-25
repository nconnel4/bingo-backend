from functools import lru_cache

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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

origins = [
    "http://localhost:5173",
    "https://polite-dune-04083480f.3.azurestaticapps.net/",
    "https://bingo.basepointdesign.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
