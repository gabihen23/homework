import pytest
import requests
import json
import jsonpath

name = "Gabi Hen"
id = 14
json_user_object = {
    "name": name,
    "id": id
}
url = "http://localhost:5000/users"
url_with_id = url + "/" + str(id)


# test_TC07_create_user_with_same_id
def test_TC07_create_user_with_same_id():
    # create_user
    response = requests.post(url, json=json_user_object)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, "id")
    user_name = jsonpath.jsonpath(json_response, "name")
    assert user_id[0] == id
    assert user_name[0] == name
    assert response.status_code == 200

    # create_another_user_with_same_data
    response = requests.post(url, json=json_user_object)
    assert response.status_code == 500


# test_TC08_create_user_with_string_for_id
def test_TC08_create_user_with_string_for_id():
    json_user_object_edit = {
        "name": "Gabi Hen",
        "id": "some text"
    }
    response = requests.post(url, json=json_user_object_edit)
    assert response.status_code == 500


# test_TC09_create_user_with_double_for_id
def test_TC09_create_user_with_double_for_id():
    json_user_object_edit = {
        "name": "Gabi Hen",
        "id": 2.3
    }
    response = requests.post(url, json=json_user_object_edit)
    assert response.status_code == 500


# test_TC10_create_user_with_negative_int_for_id
def test_TC10_create_user_with_negative_int_for_id():
    json_user_object_edit = {
        "name": "Gabi Hen",
        "id": -78
    }
    response = requests.post(url, json=json_user_object_edit)
    assert response.status_code == 500
