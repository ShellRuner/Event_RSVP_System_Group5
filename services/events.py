import os
import uuid
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from models import Event, RSVP
from schemas import EventCreate, RSVPBase

FLYERS_FOLDER = "flyers"
os.makedirs(FLYERS_FOLDER, exist_ok=True)


def create_event(db: Session, event: EventCreate, flyer: UploadFile | None):
    flyer_path = None
    if flyer:
        file_ext = flyer.filename.split('.')[-1].lower()
        if file_ext not in ['jpg', 'jpeg', 'png', 'pdf']:
            raise HTTPException(status_code=400, detail="Invalid file type")
        filename = f"{uuid.uuid4()}.{file_ext}"
        flyer_path = os.path.join(FLYERS_FOLDER, filename)
        with open(flyer_path, "wb") as f:
            f.write(flyer.file.read())

    db_event = Event(
        title=event.title,
        description=event.description,
        date=event.date,
        location=event.location,
        flyer=flyer_path
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session):
    return db.query(Event).all()


def rsvp_event(db: Session, event_id: int, rsvp: RSVPBase):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")

    db_rsvp = RSVP(name=rsvp.name, email=rsvp.email, event_id=event_id)
    db.add(db_rsvp)
    db.commit()
    db.refresh(db_rsvp)
    return db_rsvp


def get_rsvps(db: Session, event_id: int):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")

    return db.query(RSVP).filter(RSVP.event_id == event_id).all()
