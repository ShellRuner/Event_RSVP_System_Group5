from fastapi import FastAPI
from Event_RSVP_System_Group5 import models
from routers.events import router
from database import engine, Base

app = FastAPI(title="Event RSVP system",
              description="A RSVP system for events where users can create events and RSVP to them.",
              version="1.0.0",)

# home


@app.get("/")
def home():
    return "WELCOME TO RSVP SYSTEM ASSIGNMENT"


app.include_router(router, prefix="/events", tags=["Events"])

models.Base.metadata.create_all(bind=engine)
