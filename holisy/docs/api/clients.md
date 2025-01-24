**URL** : `/clients/`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Clients": [
    {
        "user_id": 5,
        "password": "123456",
        "last_login": null,
        "is_superuser": false,
        "username": "maks",
        "first_name": "Maks",
        "last_name": "Zinin",
        "email": "maks@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-10T18:35:55Z",
        "birth_date": "2021-05-19",
        "post": null,
        "salary": null,
        "phone": "+79076549876",
        "groups": [],
        "user_permissions": []
    },
    {
        "user_id": 7,
        "password": "123456",
        "last_login": null,
        "is_superuser": false,
        "username": "egor1",
        "first_name": "Egor",
        "last_name": "Kretinin",
        "email": "egor@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-10T19:08:56.765651Z",
        "birth_date": "1212-12-12",
        "post": null,
        "salary": null,
        "phone": "+79012345678",
        "groups": [],
        "user_permissions": []
    },
    {
        "user_id": 8,
        "password": "pbkdf2_sha256$260000$Z3vfAID8swe8ula2j0LWD1$LrgOZcMgJhaL1cMEIoTx54eMZWg1E9mIdss4RUprUKs=",
        "last_login": null,
        "is_superuser": false,
        "username": "Artem",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-15T08:55:07.176816Z",
        "birth_date": null,
        "post": null,
        "salary": null,
        "phone": "",
        "groups": [],
        "user_permissions": []
    }
]
}
```