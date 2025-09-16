import requests


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


def test_get_author(mock_requests_post):
    created_author = create_author()
    response = requests.get(f"http://127.0.0.1:8000/api/authors/{created_author['id']}")
    
    request_headers = {
        "Accept": "application/json",
    }
    response = requests.get(f"http://127.0.0.1:8000/api/authors/{created_author['id']}", headers=request_headers)

    assert response.status_code == 200
    assert response.json() == created_author
    

# s = requests.Session()
# s.get("https://url")

# with requests.Session() as session:
#     session.get("https://url")