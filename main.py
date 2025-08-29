from fastapi import FastAPI
from database import engine
from models import Base
from api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event RSVP system",
    description="A RSVP system for events where users can create events and RSVP to them.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"Welcome to our Event RSVP system "}


app.include_router(router)
