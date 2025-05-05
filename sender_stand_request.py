# sender_stand_request.py

import configuration
import requests
import data
import copy

# Función para crear un nuevo kit de cliente
def post_new_client_kit(kit_body, auth_token=None):
    body = copy.deepcopy(kit_body)  # Usamos una copia para no modificar el original
    headers = data.headers.copy()
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=headers
    )

# Función para obtener un nuevo authToken creando un usuario
def get_new_user_token():
    user_body = {
        "firstName": "Andrea",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    }
    response = requests.post(
        configuration.URL_SERVICE + "/api/v1/users/",
        json=user_body,
        headers=data.headers
    )
    return response.json()["authToken"]
