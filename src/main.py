from fastapi import FastAPI
from database.db import init

from fastapi import FastAPI
from models.feed import Feed
from database.db import SessionDep
from sqlmodel import select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init()

@app.get("/feeding/feed/{type}")
async def get_feed(type: str, session: SessionDep):
    feeds = session.exec(select(Feed).where(Feed.type == type)).all()
    return feeds

@app.post("/feeding/feed/{type}")
async def add_feed(id: int, type: str, amount: int, session: SessionDep):
    feed = Feed(id=id, type=type, amount=amount)
    session.add(feed)
    session.commit()
    session.refresh(feed)
