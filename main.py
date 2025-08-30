from fastapi import FastAPI
from routers.events import event_router
from database import engine, Base

app = FastAPI(title="Event RSVP system",
    description="A RSVP system for events where users can create events and RSVP to them.",
    version="1.0.0",)

#home
@app.get("/")
def home():
    return "WELCOME TO RSVP SYSTEM ASSIGNMENT"


app.include_router(event_router, prefix= "/events", tags=["Events"])

Base.metadata.create_all(bind=engine)

