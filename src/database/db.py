from typing import Annotated

from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends

engine = create_engine(f'postgresql://postgres:postgres@localhost:5433/postgres')
SQLModel.metadata.create_all(engine)

def init():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
