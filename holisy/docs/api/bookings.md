**URL** : `/bookings/`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Bookings": [
    {
        "booking_id": 1,
        "status": "На подтверждении",
        "arrival_date": "2021-06-17",
        "departure_date": "2021-06-19",
        "person_count": 2,
        "result_cost": 0,
        "client_id": 1,
        "room_number": 2,
        "services": []
    },
    {
        "booking_id": 2,
        "status": "В процессе",
        "arrival_date": "2021-06-17",
        "departure_date": "2021-06-19",
        "person_count": 2,
        "result_cost": 0,
        "client_id": 8,
        "room_number": 2,
        "services": []
    }
]
}
```