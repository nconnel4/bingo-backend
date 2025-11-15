from sqlalchemy.orm import Mapped, mapped_column, WriteOnlyMapped, relationship

from bingo_backend.database.core import Base


class Space(Base):
    __tablename__ = "spaces"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    weight: Mapped[int]

    card_spaces: WriteOnlyMapped["CardSpace"] = relationship(back_populates="space")