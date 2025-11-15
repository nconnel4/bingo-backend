from uuid import UUID, uuid4

from sqlalchemy import UniqueConstraint, ForeignKey

from bingo_backend.database.core import Base
from sqlalchemy.orm import  mapped_column, relationship, Mapped


class CardSpace(Base):
    __tablename__ = "cardspaces"
    __table_args__ = (UniqueConstraint("card_id", "position"), UniqueConstraint("space_id", "card_id"))

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    position: Mapped[int]
    is_complete: Mapped[bool] = mapped_column(default=False)
    card_id: Mapped[UUID] = mapped_column(ForeignKey("cards.id", ondelete="CASCADE"))
    space_id: Mapped[int] = mapped_column(ForeignKey("spaces.id", ondelete="CASCADE"))

    card: Mapped["Card"] = relationship(lazy="joined", back_populates="spaces")
    space: Mapped["Space"] = relationship(lazy="joined", back_populates="card_spaces")