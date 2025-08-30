from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form, UploadFile, HTTPException, status
from services.events import Event_CRUD
from database import get_db
from schemas import EventResponse
# from database import db_dependency
from sqlalchemy.orm import Session




event_router = APIRouter()

#creat a new event
@event_router.post("/", status_code= 201)
# db : db_dependency,
async def creat_event(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    date: Annotated[str, Form()],
    location: Annotated[str, Form()],
    flyer: Optional[UploadFile] = None,
    db : Session = Depends(get_db)
):
    # flyer_filename = None
    
    if flyer:
        flyer_filename = flyer.filename
        await save_file_to_disk(flyer)
    else:
        flyer_filename = None
    event = Event_CRUD.creat_event(db, title, description, date, location, flyer_filename)
    
    return {"data" : event, "message" : "Event created successfully"}

async def save_file_to_disk(uploaded_file: UploadFile):
    with open(uploaded_file.filename, "wb+") as file_object:
        file_content = await uploaded_file.read()
        file_object.write(file_content)

@event_router.get("/", status_code= status. HTTP_200_OK)
async def get_all_events(db: Session = Depends(get_db)):
    try: 
        events= Event_CRUD.get_all_events(db)
        return {"data": events}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@event_router.get("/{book_id}", status_code= status.HTTP_200_OK)
async def get_event_by_id(book_id: int, db: Session= Depends(get_db)):
    try:
        event = Event_CRUD.get_event(db, book_id)
        if event:
            return event
        
    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))
    
        
    
        