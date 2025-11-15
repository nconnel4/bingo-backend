from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import Annotated

from bingo_backend.cardspace.services import toggle_complete
from uuid import UUID

from bingo_backend.database.core import get_session

router = APIRouter(prefix="/cardspaces")

@router.put("/{space_id}/complete")
def toggle_complete_space(space_id: UUID, session: Session = Depends(get_session)):
    toggle_complete(session=session, space_id=space_id)