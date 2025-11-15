from fastapi import APIRouter
from bingo_backend.card.routes import router as card_router
from bingo_backend.cardspace.routes import router as card_space_router

router = APIRouter(prefix="/api")

router.include_router(card_router, prefix="/cards")
router.include_router(card_space_router)