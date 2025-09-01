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
        
    @staticmethod
    def get_rsvp_for_event(db : Session, event_id : UUID):
        result = db.query(RSVP.event_id).filter(RSVP.event_id == str(event_id)).first()
        if result[0]:
            db_rsvps = db.query(RSVP).filter(RSVP.event_id == str(event_id)).all()
            return db_rsvps
        else:
            return {"message" : "This event don't exist"}
                
            
        
rsvp_services = RSVPServices()