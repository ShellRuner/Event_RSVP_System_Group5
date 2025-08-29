import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    date = Column(String)
    location = Column(String)
    flyer = Column(String, nullable=True)
    rsvps = relationship("RSVP", back_populates="event")


class RSVP(Base):
    __tablename__ = "rsvps"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="rsvps")
