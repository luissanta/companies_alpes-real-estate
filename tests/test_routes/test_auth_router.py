from httpx import Response


def test_login_successful(client):
    _login = login(client, {"username": "admin", "password": "admin"})

    assert _login.status_code == 200
    assert "access_token" in _login.json()
    assert "token_type" in _login.json()


def login(client, login_data) -> Response:
    response = client.post("/api/v1/auth/login", data=login_data)
    return response
