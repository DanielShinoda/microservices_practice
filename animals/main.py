from fastapi import FastAPI
from database.db import wait_for_db

from models.animals import Animals
from database.db import SessionDep
from sqlmodel import select
import requests


app = FastAPI()


@app.on_event("startup")
def on_startup():
    wait_for_db()


@app.get("/animals")
async def animal(session: SessionDep):
    animals = session.exec(select(Animals)).all()
    return animals


@app.post("/animals")
async def add_animal(
    id: int, name: str, type: str, feed_type: str, session: SessionDep
):
    animal = Animals(id=id, name=name, type=type, feed_type=feed_type)
    session.add(animal)
    session.commit()
    session.refresh(animal)


@app.post("/animals/feed/{name}")
async def animal(name: str, session: SessionDep):
    animal = session.exec(select(Animals).where(Animals.name == name)).one_or_none()
    if not animal:
        return

    response = requests.get(f"http://feed:8001/feeding/feed/{animal.feed_type}")
    return response.json()
