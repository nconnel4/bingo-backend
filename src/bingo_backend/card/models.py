from uuid import UUID, uuid4

from bingo_backend.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[UUID] = mapped_column(default=uuid4,primary_key=True)
    user: Mapped[str]

    spaces: Mapped[list["CardSpace"]] = relationship(lazy="joined", back_populates="card")





