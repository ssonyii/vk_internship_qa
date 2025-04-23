import requests, pytest
from config import BASE_URL, HEADERS, VALID_LOGIN, INVALID_LOGIN

def test_successful_authentication():
    r = requests.post(f"{BASE_URL}/users/login", json=VALID_LOGIN)
    assert r.status_code == 200
    assert "Token" in r.headers

# 1 Сценарий
def test_failed_authentication_wrong_credentials():
    r = requests.post(f"{BASE_URL}/users/login", json=INVALID_LOGIN)
    assert r.status_code == 401

# 2 Сценарий
def get_user_by_email(email):
    return requests.get(f"{BASE_URL}/users/email/{email}", headers=HEADERS)

def deactivate_user(user_id):
    return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

def ensure_user_is_blocked(email):
    response = get_user_by_email(email)
    if response.status_code == 200:
        user_id = response.json()["id"]
        deactivate_user(user_id)

def test_failed_authentication_blocked_user():
    email = "blocked@example.com"
    password = "blockedpassword"

    ensure_user_is_blocked(email)
    
    blocked = {"login_id": email, "password": password}

    r = requests.post(f"{BASE_URL}/users/login", json=blocked)
    assert r.status_code == 401

# 4 Сценарий
def test_failed_authentication_inactive_user():
    # Предполагается, что пользователь не активирован
    inactive = {"login_id": "inactive@example.com", "password": "somepass"}
    r = requests.post(f"{BASE_URL}/users/login", json=inactive)
    assert r.status_code == 401

# Mattermost возвращает 401 для неактивных/заблокированных пользователей

# 3 Сценарий
def test_failed_authentication_no_server(monkeypatch):
    def mock_post(*args, **kwargs):
        raise ConnectionError("Отсутствие соединения с сервером аутентификации")
    
    monkeypatch.setattr(requests, "post", mock_post)

    with pytest.raises(ConnectionError):
        requests.post(f"{BASE_URL}/users/login", json=VALID_LOGIN)