from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends
from sqlalchemy.orm import Session

from bingo_backend.cardspace.flows import check_bingo
from bingo_backend.cardspace.services import toggle_complete
from uuid import UUID

from bingo_backend.database.core import get_session

router = APIRouter(prefix="/cardspaces")

@router.put("/{space_id}/complete")
def toggle_complete_space(space_id: UUID,  background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    background_tasks.add_task(check_bingo, session=session, space_id=space_id)
    toggle_complete(space_id=space_id, session=session)