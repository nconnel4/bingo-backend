from fastapi import APIRouter, Depends
from uuid import UUID

from bingo_backend.card.dtos import CardRead
from bingo_backend.card.services import get_card_by_id
from bingo_backend.database.core import get_session

router = APIRouter()

@router.get("/{card_id}", response_model=CardRead)
def get_card(card_id: UUID, session=Depends(get_session)):
    return get_card_by_id(session=session, card_id=card_id)