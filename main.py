from fastapi import FastAPI
from routers.events import event_router
from database import engine, Base

app = FastAPI()

#home
@app.get("/")
def home():
    return "WELCOME TO RSVP SYSTEM ASSIGNMENT"


app.include_router(event_router, prefix= "/events", tags=["Events"])

Base.metadata.create_all(bind=engine)

