import requests
import json


class ReferenceApi(object):

    url = "https://api-referencias.proyecto2019.linti.unlp.edu.ar"

    @classmethod
    def all_documents(cls):
        response = requests.get(cls.url + "/tipo-documento")
        data = response.text
        return json.loads(data)

    @classmethod
    def all_locations(cls):
        response = requests.get(cls.url + "/localidad")
        data = response.text
        return json.loads(data)

    @classmethod
    def find_document_type_name(cls, id):
        response = requests.get(cls.url + "/tipo-documento/" + str(id))
        data = response.text
        return json.loads(data)["nombre"]

    @classmethod
    def find_location_name(cls, id):
        response = requests.get(cls.url + "/localidad/" + str(id))
        data = response.text
        return json.loads(data)["nombre"]
