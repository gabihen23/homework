import pytest
import requests
import json
import jsonpath

name = "Gabi Hen"
id = 10
json_user_object = {
    "name": name,
    "id": id
}
url = "http://localhost:5000/users"
url_with_id = url + "/" + str(id)


# test_TC01_TC02_TC03_get_all_users_and_add_new_user_and_validate_amount
def test_TC01_TC02_TC03_get_all_users_and_add_new_user_and_validate_amount():
    # test_TC01_get_all_users
    response = requests.get(url)
    json_response = response.json()
    users_amount = len(json_response)
    assert response.status_code == 200

    # test_TC02_Add_new_user
    response = requests.post(url, json=json_user_object)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, "id")
    user_name = jsonpath.jsonpath(json_response, "name")
    assert user_id[0] == id
    assert user_name[0] == name
    assert response.status_code == 200

    # test_TC03_validate_user_amount_increased
    response = requests.get(url)
    json_response = response.json()
    new_users_amount = len(json_response)
    assert response.status_code == 200
    assert new_users_amount == users_amount + 1


# test_TC04_get_user_data
def test_TC04_get_user_data():
    response = requests.get(url_with_id)
    json_response = response.json()
    user_id = jsonpath.jsonpath(json_response, "id")
    user_name = jsonpath.jsonpath(json_response, "name")
    assert user_id[0] == id
    assert user_name[0] == name
    assert response.status_code == 200


# test_TC04_update_user_data
def test_TC05_update_user_data():
    json_user_object_edit = {
        "name": "Omer Hen",
        "id": id
    }
    response = requests.put(url_with_id, json=json_user_object_edit)
    json_response = response.json()
    user_name = jsonpath.jsonpath(json_response, "name")
    assert user_name[0] == json_user_object_edit.get("name")
    assert response.status_code == 201


# test_TC06_delete_user and validate the amount of users
def test_TC06_delete_user():
    # get amount of users
    response = requests.get(url)
    json_response = response.json()
    users_amount = len(json_response)

    # delete the user
    response = requests.delete(url_with_id)
    json_response = response.json()
    assert response.status_code == 200
    assert len(json_response) == users_amount - 1
