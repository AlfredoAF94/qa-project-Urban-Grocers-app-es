#create_user_test.py

import sender_stand_request
import data
import pytest

# Función para validar casos positivos
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función para validar casos negativos
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_new_user_token())
    assert response.status_code == 400
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Prueba 1
def test_create_kit_with_short_name():
    positive_assert(data.kit_body_1)

# Prueba 2
def test_create_kit_with_valid_name():
    positive_assert(data.kit_body_2)

# Prueba 3
def test_create_kit_with_empty_name():
    negative_assert_code_400(data.kit_body_3)

# Prueba 4
def test_create_kit_with_too_long_name():
    negative_assert_code_400(data.kit_body_4)

# Prueba 5
def test_create_kit_with_special_characters():
    positive_assert(data.kit_body_5)

# Prueba 6
def test_create_kit_with_space_characters():
    positive_assert(data.kit_body_6)

# Prueba 7
def test_create_kit_with_numbers_characters():
    positive_assert(data.kit_body_7)

# Prueba 8
def test_create_kit_with_missing_name():
    kit_body = {}
    negative_assert_code_400(kit_body)

# Prueba 9
def test_create_kit_with_name_as_number():
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body)
