import uuid
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Event, RSVP


class RSVPServices:
    @staticmethod
    def rsvp_to_an_event(db : Session, event_id : UUID, name : str, email : str):
        if db.query(Event.id).filter(Event.id == str(event_id)).first():
            try:
                result = db.query(Event.id).filter(Event.id == str(event_id)).first()
                db_rsvp = RSVP(id = str(uuid.uuid4()), name=name, email=email, event_id=result[0])
                db.add(db_rsvp)
                db.commit()
                db.refresh(db_rsvp)
                return (db_rsvp)
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code = 500, detail=str(e))
            
        # else:
        #     return {"message" : "This event don't exist"}
        
rsvp_services = RSVPServices()