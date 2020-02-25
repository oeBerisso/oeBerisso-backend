rules = {
    "last_name": {"presence": True, "name": "apellido"},
    "first_name": {"presence": True, "name": "nombre"},
    "gender": {"presence": True, "name": "genero"},
    "document_type": {"presence": True, "name": "Tipo de documento"},
    "number": {"presence": True, "type_number": True, "name": "numero de documento"},
    "birth_date": {"presence": True, "name": "Fecha de nacimiento"},
    "location": {"presence": True, "name": "localidad"},
    "home": {"presence": True, "name": "domicilio"},
    "phone": {"presence": True, "type_number": True, "name": "numero de telefono"},
}
