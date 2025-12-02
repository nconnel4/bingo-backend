import random

from bingo_backend.bingo.models import BingoGif

def get_bingo_gif(*, session):
    gifs = session.query(BingoGif)

    return random.choice([gif for gif in gifs])
