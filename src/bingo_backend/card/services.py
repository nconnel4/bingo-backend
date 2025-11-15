from uuid import UUID

from bingo_backend.database.core import SessionLocal
from bingo_backend.card.models import Card

def get_card_by_id(*, session, card_id: UUID) -> Card:
    return session.query(Card).where(Card.id == card_id).one_or_none()