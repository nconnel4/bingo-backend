from time import sleep

from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.orm import Session
from uuid import UUID

from bingo_backend.cardspace.dtos import CardSpaceRead
from bingo_backend.cardspace.flows import check_bingo
from bingo_backend.cardspace.services import toggle_complete, get_card_spaces_by_card_id
from bingo_backend.database.core import get_session

router = APIRouter(prefix="/cardspaces")

@router.put("/{space_id}/complete")
def toggle_complete_space(space_id: UUID,  background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    background_tasks.add_task(check_bingo, session=session, space_id=space_id)
    toggle_complete(space_id=space_id, session=session)

@router.get("/{card_id}", response_model=CardSpaceRead)
def get_card_spaces(card_id: UUID, session: Session = Depends(get_session)):
    return get_card_spaces_by_card_id(session=session, card_id=card_id)
