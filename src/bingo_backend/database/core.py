from typing import Generator

from sqlalchemy import create_engine, make_url, MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from bingo_backend.main import get_settings


def create_db_engine(connection_string: str):
    url = make_url(connection_string)
    return create_engine(url, echo=True)

engine = create_db_engine(get_settings().connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    """Get a db session."""
    with SessionLocal() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            session.rollback()
            raise e

Base = declarative_base()