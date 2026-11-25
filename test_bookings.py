
import httpx

BASE_URL = "http://127.0.0.1:8000"

# 1. Create Booking
booking = {
    "room_id": "B205",
    "date": "2026-11-27",
    "start_hour": 10,
    "end_hour": 12,
    "purpose": "Study"
}

response = httpx.put(
    f"{BASE_URL}/bookings/BK100",
    json=booking
)

print("Create Booking:", response.status_code)
print(response.json())


# 2. Get Booking
response = httpx.get(
    f"{BASE_URL}/bookings/BK100"
)

print("Get Booking:", response.status_code)
print(response.json())


# 3. Conflict Booking
conflict_booking = {
    "room_id": "B205",
    "date": "2026-11-27",
    "start_hour": 11,
    "end_hour": 13,
    "purpose": "Another Study"
}

response = httpx.put(
    f"{BASE_URL}/bookings/BK101",
    json=conflict_booking
)

print("Conflict Booking:", response.status_code)
print(response.json())


# 4. Invalid Room
invalid_booking = {
    "room_id": "X999",
    "date": "2026-11-28",
    "start_hour": 10,
    "end_hour": 12,
    "purpose": "Test"
}

response = httpx.put(
    f"{BASE_URL}/bookings/BK102",
    json=invalid_booking
)

print("Invalid Room:", response.status_code)
print(response.json())


# 5. Invalid Hours
invalid_hours = {
    "room_id": "B205",
    "date": "2026-11-28",
    "start_hour": 15,
    "end_hour": 12,
    "purpose": "Invalid Hours"
}

response = httpx.put(
    f"{BASE_URL}/bookings/BK103",
    json=invalid_hours
)

print("Invalid Hours:", response.status_code)
print(response.json())


# 6. Delete Booking
response = httpx.delete(
    f"{BASE_URL}/bookings/BK100"
)

print("Delete Booking:", response.status_code)
