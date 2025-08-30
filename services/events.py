import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Event, RSVP
# from database import db_dependency
from uuid import UUID

class EventServices:
    @staticmethod
    def creat_event(db : Session , title : str, description : str, date : str, location : str, flyer_filename : str):
        try:
            db_event = Event(id=str(uuid.uuid4()), title = title, description=description, date=date, location=location, flyer_filename=flyer_filename)
        
            db.add(db_event)
            db.commit()
            db.refresh(db_event)
            return(db_event)
        except Exception as e:
            db.rollback()
            
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_all_events(db : Session):
        return db.query(Event).all()
    
    @staticmethod
    def rsvp_to_an_event(db : Session, event_id : UUID, name : str, email : str):
        if db.query(Event.id).filter(Event.id == str(event_id).firt()):
            try:
                result = db.query(Event.id).filter(Event.id == str(event_id).firt())
                db_rsvp = RSVP(id = str(uuid.uuid4()), name=name, email=email, event_id=result[0])
                db.add(db_rsvp)
                db.commit()
                db.refresh(db_rsvp)
                return (db_rsvp)
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code = 500, detail=str(e))
            
        else:
            return {"message" : "This event don't exist"}
            
            
    
    @staticmethod
    def get_all_events(db: Session):
        db.query(Event).all()

    @staticmethod
    def get_event(db:Session, event_id: int):
        db.query(Event).filter(Event.id == event_id).first()
    
Event_CRUD = EventServices()


        