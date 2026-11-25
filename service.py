from fastapi import FastAPI, HTTPException, Response
from datetime import date
from pydantic import BaseModel, Field, model_validator
app = FastAPI()
class Room(BaseModel):
    id: str
    building: str
    capacity: int

class Booking(BaseModel):
    room_id: str
    date: date
    start_hour: int = Field(ge=8, le=20)
    end_hour: int = Field(ge=8, le=20)
    purpose: str

    @model_validator(mode="after")
    def check_hours(self):
        if self.end_hour <= self.start_hour:
            raise ValueError("End hour must be after start hour")
        return self
rooms = {
    "B205": {
        "id": "B205",
        "building": "Engineering",
        "capacity": 30
    },
    "A101": {
        "id": "A101",
        "building": "Science",
        "capacity": 20
    }
}
bookings = {}
@app.get("/rooms")
def get_rooms():
    return list(rooms.values())
@app.post("/rooms", status_code=201)
def create_room(room: Room):
    if room.id in rooms:
        raise HTTPException(status_code=409, detail="Room already exists")

    rooms[room.id] = room.model_dump()
    return rooms[room.id]  
@app.get("/rooms/{room_id}")
def get_room(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")

    return rooms[room_id]
@app.put("/bookings/{booking_id}")
def create_booking(booking_id: str, booking: Booking, response: Response):

    new_booking = booking.model_dump(mode="json")

    if booking_id in bookings:
        if bookings[booking_id] == new_booking:
            response.status_code = 200
            return bookings[booking_id]

        raise HTTPException(
            status_code=409,
            detail="Booking ID already exists with different data"
        )

    if booking.room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")

    for old_booking in bookings.values():
        if (
            old_booking["room_id"] == booking.room_id
            and old_booking["date"] == str(booking.date)
            and booking.start_hour < old_booking["end_hour"]
            and booking.end_hour > old_booking["start_hour"]
        ):
            raise HTTPException(
                status_code=409,
                detail="Booking conflict"
            )

    response.status_code = 201
    bookings[booking_id] = new_booking

    return bookings[booking_id]


@app.get("/bookings")
def get_bookings():
    return list(bookings.values())
@app.get("/bookings/{booking_id}")
def get_booking(booking_id: str):
    if booking_id not in bookings:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return bookings[booking_id]
@app.delete("/bookings/{booking_id}", status_code=204)
def delete_booking(booking_id: str):
    if booking_id not in bookings:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    del bookings[booking_id]
    return    