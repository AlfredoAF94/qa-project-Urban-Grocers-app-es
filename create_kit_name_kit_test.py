#create_user_test.py

import sender_stand_request
import data
import pytest

#Prueba 1
def test_create_kit_with_short_name():
    kit_body = {
        "name": "a"
    }
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

#Prueba 2
def test_create_kit_with_valid_name():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    }
    token = sender_stand_request.get_new_user_token()  # Obtener el token
    response = sender_stand_request.post_new_client_kit(kit_body, token)  # Enviar con token

    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]








