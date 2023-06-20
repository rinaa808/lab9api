from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from app import settings

engine = create_engine(settings.database_url, echo=True)


def get_session() -> Session:
    with Session(engine) as session:
        yield session


Base = declarative_base()