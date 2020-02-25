rules = {
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
