from fastapi import APIRouter, Form, UploadFile, File, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import Event, EventCreate, RSVP, RSVPBase
from services.events import create_event, get_events, rsvp_event, get_rsvps

router = APIRouter()


@router.post("/", response_model=Event)
async def create_event_route(
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    flyer: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    event_create = EventCreate(
        title=title, description=description, date=date, location=location)
    return create_event(db, event_create, flyer)


@router.get("/", response_model=List[Event])
def get_events_route(db: Session = Depends(get_db)):
    return get_events(db)


@router.post("/{event_id}/rsvp", response_model=RSVP)
def rsvp_event_route(
    event_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    rsvp_create = RSVPBase(name=name, email=email, event_id=id)
    return rsvp_event(db, event_id, rsvp_create)


@router.get("/{event_id}/rsvps", response_model=List[RSVP])
def get_rsvps_route(event_id: int, db: Session = Depends(get_db)):
    return get_rsvps(db, event_id)
