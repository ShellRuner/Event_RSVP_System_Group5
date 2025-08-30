from sqlalchemy import Column, String, Float, Integer
from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable = False)
    description = Column(String, nullable=False)
    date = Column(String, nullable=False)
    location = Column(String, nullable=False)
    flyer_filename = Column(String, nullable=True)
    

class RSVP(Base):
    __tablename__ = "rsvp"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(Integer, nullable=False)

