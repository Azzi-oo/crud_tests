import pytest
import requests


def test_create_author_initial(mock_requests_post):
    request_body = {
        "age": 0,
        "name": "test",
        "genre": "test",
        "dateOfBirth": "",
        "dateOfDeath": "",
        "dead": False,
    }
    response = requests.post("http://127.0.0.1:8000/api/authors/create", json=request_body)
    data = response.json()
    deserialized_response = response.json()

    assert response.status_code == 201
    assert data["name"] == request_body["name"]
    assert data["age"] == int(request_body["age"])  # coerced to int by fake
    assert data["genre"] == request_body["genre"]
    assert data["dead"] is request_body["dead"]
    assert deserialized_response["name"] == request_body["name"]
    assert deserialized_response["age"] == request_body["age"]


def create_author():
    request_body = {
        "age": 0,
        "name": "test",
        "genre": "test",
        "dateOfBirth": "",
        "dateOfDeath": "",
        "dead": False,
    }
    response = requests.post("http://127.0.0.1:8000/api/authors/create", json=request_body)
    return response.json()


def test_create_author(mock_requests_post):
    created_author = create_author()
    response = requests.get(f"http://127.0.0.1:8000/api/authors/{created_author['id']}")

    assert response.status_code == 200
    assert response.json() == created_author


def test_get_author(mock_requests_post):
    created_author = create_author()
    response = requests.get(f"http://127.0.0.1:8000/api/authors/{created_author['id']}")

    assert response.status_code == 200
    assert response.json() == created_author


def test_update(mock_requests_post):
    created_author = create_author()

    update_request_body = {
        "age": 55,
        "name": "Updated Name",
        "genre": "Genre",
        "dateOfBirth": "00.11.22",
        "dateOfDeath": "22.33.44",
        "dead": True,
    }

    response = requests.put(f"http://127.0.0.1:8000/api/authors/{created_author['id']}", json=update_request_body)
    parsed_response = response.json()

    assert response.status_code == 200
    assert parsed_response["id"]
    tmp_id = parsed_response["id"]
    del parsed_response["id"]
    assert parsed_response == update_request_body


def test_delete(mock_requests_post):
    created_author = create_author()
    response = requests.delete(f"http://127.0.0.1:8000/api/authors/{created_author['id']}")

    assert response.status_code == 200
    assert response.json() == created_author


# def some_decorator(function):
#     def wrapper():
#         print("before func")
#         function()
#         print("After func")
#     return wrapper


# @some_decorator
# def setup_module():
#     print("setup")

# @pytest.fixture(scope="function", autouse=True)
# def test_first_test():
#     assert 1 == 1


# def teardown():
#     print("teardown")