from typing import Annotated

from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
import os
from sqlalchemy.exc import OperationalError
import time

engine = create_engine(os.environ["DATABASE_URL"])
SQLModel.metadata.create_all(engine)


def wait_for_db():
    retries = 5
    while retries:
        try:
            SQLModel.metadata.create_all(engine)
            return
        except OperationalError:
            retries -= 1
            time.sleep(5)
    raise Exception("Failed to connect to database after multiple attempts")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
