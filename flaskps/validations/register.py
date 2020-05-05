rules = {
    "username": {
        "presence": True,
        "unique_user": True,
        "not_google_username": True,
        "name": "usuario"
    },
    "last_name": {"presence": True, "name": "apellido"},
    "first_name": {"presence": True, "name": "nombre"},
    "email": {"presence": True, "email": True, "unique_mail": True, "name": "email"},
    "password": {
        "presence": True,
        "min_length": 6,
        "name": "contraseña",
    },
    "confirm_password": {
        "presence": True,
        "min_length": 6,
        "name": "confirmar contraseña",
        "compare_fields": "password",
    },
}
