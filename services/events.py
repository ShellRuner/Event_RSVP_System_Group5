from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Event
# from database import db_dependency
import uuid

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
    
    
Event_CRUD = EventServices()
        