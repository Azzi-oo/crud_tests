from pretenders.client.http import HttpMock

mock = HTTPMock("localhost", 8000)

def setup_ok():
    mock.reset()
    mock.when("GET /admins_online?someParam=someValue").reply('{"Result": "OK"}', status=200)
    
def test_mock():
    setup_ok()
    mock_url = mock.pretend_access_point + mock.pretend_access_path
    
    response = requests.get(f"http://{mock_url}/admins_online")
    assert response.text == '{"Result": "OK"}'