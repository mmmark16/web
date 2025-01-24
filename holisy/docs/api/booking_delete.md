**URL** : `/booking/delete/<int:pk>`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : IsAudmin

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
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
}
```