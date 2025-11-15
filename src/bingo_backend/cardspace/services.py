from sqlalchemy.orm import Session

from bingo_backend.cardspace.models import CardSpace
from uuid import UUID

def get_card_space(*, session: Session, space_id: UUID):
        return session.query(CardSpace).filter(CardSpace.id == space_id).one_or_none()

def toggle_complete(*, session: Session, space_id: UUID):
    card_space = get_card_space(session=session, space_id=space_id)

    card_space.is_complete = not card_space.is_complete
    session.commit()