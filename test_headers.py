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
    

def test_with_session():
    try:
        with requests.Session() as session:
            # Для тестирования используйте реальный URL
            response = session.get(
                "https://httpbin.org/json",  # Тестовый URL
                timeout=10,
                headers={'User-Agent': 'test-script'}
            )
            response.raise_for_status()
            print("Success!")
            
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения - проверьте интернет")
    except requests.exceptions.Timeout:
        print("Таймаут запроса")
    except Exception as e:
        print(f"Другая ошибка: {e}")