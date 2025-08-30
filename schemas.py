from pydantic import BaseModel
from typing import Optional
from fastapi import Form

#Events Schemas

class EventCreate(BaseModel):
    title : str=Form(...)
    descrioption : str
    date : str
    location : str
    flyer_filename : Optional[str] = None
    
class EventUpdate(EventCreate):
    pass

class Event(EventCreate):
    id : int
    
    

class EventResponse(Event):
    pass

##RSVP schemas
class RSVPBase(BaseModel):
    name : str
    email : str
    event_id : int

class RSVPUpdate(RSVPBase):
    pass

class RSVP(RSVPBase):
    id : int