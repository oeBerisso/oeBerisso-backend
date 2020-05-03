rules = {
    "username": {"presence": True, "unique_user": True, "name": "usuario"},
    "last_name": {"presence": True, "name": "apellido"},
    "first_name": {"presence": True, "name": "nombre"},
    "email": {"presence": True, "email": True, "unique_mail": True, "name": "email"},
    "password": {
        "presence": True,
        "min_length": 6,
        "compare_fields": "confirm_password",
        "name": "contraseña",
    },
    "confirm_password": {
        "presence": True,
        "min_length": 6,
        "name": "confirmar contraseña",
    },
}