rules = {
    "first_name": {"presence": True, "name": "nombre"},
    "last_name": {"presence": True, "name": "apellido"},
    "email": {"presence": True, "email": True, "unique_mail": True, "name": "email"},
}
