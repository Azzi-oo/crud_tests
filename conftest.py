import pytest

@pytest.fixture
def prepare_data():
    return "test data"
    

# Added fixture to mock requests.* so tests don't hit real HTTP
@pytest.fixture
def mock_requests_post(monkeypatch):
    # simple in-memory store for authors
    store = {}
    next_id = {"value": 1}

    class FakeResponse:
        def __init__(self, status_code=200, json_data=None):
            self.status_code = status_code
            self._json_data = json_data or {}

        def json(self):
            return self._json_data

    def fake_post(url, json=None, *args, **kwargs):
        author_id = next_id["value"]
        next_id["value"] += 1
        author = {
            "id": author_id,
            "name": (json or {}).get("name", "test"),
            "age": int((json or {}).get("age", 0)),
            "genre": (json or {}).get("genre", "unknown"),
            "dateOfBirth": (json or {}).get("dateOfBirth", ""),
            "dateOfDeath": (json or {}).get("dateOfDeath", ""),
            "dead": (json or {}).get("dead", False),
        }
        store[author_id] = author
        return FakeResponse(status_code=201, json_data=author)

    def fake_get(url, *args, **kwargs):
        try:
            author_id = int(url.rstrip("/").split("/")[-1])
        except ValueError:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        author = store.get(author_id)
        if not author:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        return FakeResponse(status_code=200, json_data=author)

    def fake_put(url, json=None, *args, **kwargs):
        try:
            author_id = int(url.rstrip("/").split("/")[-1])
        except ValueError:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        existing = store.get(author_id)
        if not existing:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        updated = dict(json or {})
        updated["id"] = author_id
        store[author_id] = updated
        return FakeResponse(status_code=200, json_data=updated)

    def fake_delete(url, *args, **kwargs):
        try:
            author_id = int(url.rstrip("/").split("/")[-1])
        except ValueError:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        author = store.pop(author_id, None)
        if not author:
            return FakeResponse(status_code=404, json_data={"detail": "Not found"})
        return FakeResponse(status_code=200, json_data=author)

    import requests
    monkeypatch.setattr(requests, "post", fake_post)
    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.setattr(requests, "put", fake_put)
    monkeypatch.setattr(requests, "delete", fake_delete)
    return True
    
    
    
    