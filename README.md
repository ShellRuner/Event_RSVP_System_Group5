# Event RSVP System Backend

This is a FastAPI-based backend application for an Event RSVP System, implementing the specifications for Project 3 from the provided document. It uses SQLAlchemy ORM with a PostgreSQL database to manage events and RSVPs.

## Features
- Create events with optional flyer uploads
- List all events
- RSVP to events with name and email
- View RSVPs for a specific event
- File upload support for event flyers (jpg, jpeg, png, pdf)
- PostgreSQL database with SQLAlchemy ORM
- Environment variable configuration

## Prerequisites
- Python 3.8+
- PostgreSQL database
- pip for installing dependencies

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd event-rsvp-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the project root with the following:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/event_db
   ```
   Replace `username`, `password`, and `event_db` with your PostgreSQL credentials and database name.

4. **Set Up PostgreSQL**
   - Ensure PostgreSQL is installed and running.
   - Create a database named `event_db` (or your chosen name, matching the `DATABASE_URL`).
   ```bash
   createdb event_db
   ```

5. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

6. **Access API Documentation**
   - Open `http://localhost:8000/docs` in your browser for the interactive Swagger UI.


## API Endpoints
- **POST /events/**: Create a new event (form fields: title, description, date, location, flyer[optional])
- **GET /events/**: List all events
- **POST /events/{event_id}/rsvp**: RSVP to an event (form fields: name, email)
- **GET /events/{event_id}/rsvps**: List RSVPs for a specific event