from uuid import UUID, uuid4

from bingo_backend.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class BingoGif(Base):
    __tablename__ = "bingogifs"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    link: Mapped[str]



