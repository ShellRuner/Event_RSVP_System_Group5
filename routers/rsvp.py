from uuid import UUID
from fastapi import APIRouter, Depends, Form, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from services.rsvp import rsvp_services


rsvp_router = APIRouter()
#rsvp to an event
@rsvp_router.post("/events/{event_id}/rsvp", status_code=201)
def rsvp_to_an_event(
    event_id : Annotated[UUID, Path()], 
    name : Annotated[str, Form()],
    email: Annotated[str, Form()],
    db : Session = Depends(get_db)
    ):
    
    rsvp = rsvp_services.rsvp_to_an_event(db, event_id, name, email)
    if rsvp:
        return {"data" : rsvp, "message" : "rsvp succeffully to this event"}
    else:
        return {"message" : "This event don't exist"}
    
#Get list of rsvps for an event
@rsvp_router.get("/events/{event_id}/rsvp", status_code=200)
def get_rsvp_for_event(
    event_id : Annotated[UUID, Path()],
    db : Session = Depends(get_db)
    ):
    try:
        rsvps = rsvp_services.get_rsvp_for_event(db, event_id)
        return {"data" : rsvps}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))