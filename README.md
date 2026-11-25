# Lab Assignment 2: Campus Room Booking Service

## 1. Project Description

The Campus Room Booking Service is a REST API that allows university students and staff to manage room bookings.

The service provides operations for managing rooms and bookings. It also prevents overlapping bookings for the same room on the same day.

## 2. Technologies Used

- Python
- FastAPI
- Pydantic
- HTTPX

## 3. API Design

### API Operations

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th>Method</th>
      <th>URI</th>
      <th>Request Body</th>
      <th>Success Status</th>
      <th>Error Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Get All Rooms</td>
      <td>GET</td>
      <td><code>/rooms</code></td>
      <td>None</td>
      <td>200</td>
      <td>None expected</td>
    </tr>
    <tr>
      <td>Create Room</td>
      <td>POST</td>
      <td><code>/rooms</code></td>
      <td>Room data</td>
      <td>201</td>
      <td>422, 409</td>
    </tr>
    <tr>
      <td>Get Room by ID</td>
      <td>GET</td>
      <td><code>/rooms/{room_id}</code></td>
      <td>None</td>
      <td>200</td>
      <td>404</td>
    </tr>
    <tr>
      <td>Get All Bookings</td>
      <td>GET</td>
      <td><code>/bookings</code></td>
      <td>None</td>
      <td>200</td>
      <td>None expected</td>
    </tr>
    <tr>
      <td>Create Booking</td>
      <td>PUT</td>
      <td><code>/bookings/{booking_id}</code></td>
      <td>Booking data</td>
      <td>201 (new), 200 (retry)</td>
      <td>404, 409, 422</td>
    </tr>
    <tr>
      <td>Get Booking by ID</td>
      <td>GET</td>
      <td><code>/bookings/{booking_id}</code></td>
      <td>None</td>
      <td>200</td>
      <td>404</td>
    </tr>
    <tr>
      <td>Delete Booking</td>
      <td>DELETE</td>
      <td><code>/bookings/{booking_id}</code></td>
      <td>None</td>
      <td>204</td>
      <td>404</td>
    </tr>
  </tbody>
</table>

### Request Body Examples

#### Create Room

```json
{
  "id": "B205",
  "building": "Engineering",
  "capacity": 30
}
```

#### Create Booking

```json
{
  "room_id": "B205",
  "date": "2026-11-26",
  "start_hour": 10,
  "end_hour": 12,
  "purpose": "Study Group"
}
```

### HTTP Status Codes

<table>
  <thead>
    <tr>
      <th>Status Code</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>200</td><td>Request successful</td></tr>
    <tr><td>201</td><td>Resource created</td></tr>
    <tr><td>204</td><td>Resource deleted successfully</td></tr>
    <tr><td>404</td><td>Room or booking not found</td></tr>
    <tr><td>409</td><td>Booking conflict or duplicate resource ID</td></tr>
    <tr><td>422</td><td>Invalid request data</td></tr>
  </tbody>
</table>
 ## 4. Environment Setup

A virtual environment was created using Python's `venv` module to isolate project dependencies.

The following libraries were installed:

- FastAPI: To build the REST API.
- Uvicorn: To run the API server.
- HTTPX: To send HTTP requests and test the API.
- Pydantic: To validate request data.

The installation command was:

```bash
python -m pip install fastapi uvicorn httpx
```

## 5. Running the Application

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the FastAPI server:

```bash
python -m uvicorn service:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## 6. Testing with HTTPX

The API was tested using the `test_bookings.py` client.

Run the tests using:

```bash
python test_bookings.py
```

### Test Results

| Test Case         | Expected Status | Actual Status |
| ----------------- | --------------: | ------------: |
| Create Booking    |             201 |           201 |
| Get Booking       |             200 |           200 |
| Idempotency Retry |             200 |           200 |
| Conflict Booking  |             409 |           409 |
| Invalid Room      |             404 |           404 |
| Invalid Hours     |             422 |           422 |
| Delete Booking    |             204 |           204 |

All tests passed successfully.

### Client Output

```text
Create Booking: 201
Get Booking: 200
Conflict Booking: 409
Invalid Room: 404
Invalid Hours: 422
Delete Booking: 204
```

## 7. Idempotency

The API uses the PUT method to create bookings with a client-provided booking ID.

- First request with a new booking ID returns 201 Created.
- Repeating the same request with the same ID and data returns 200 OK.
- Using the same ID with different data returns 409 Conflict.

This prevents duplicate bookings when the same request is repeated.

## 8. Project Structure

```text
lab2-assignment/
│
├── service.py
├── test_bookings.py
├── README.md
└── .venv/
```
