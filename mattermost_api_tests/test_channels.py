import requests, pytest
from config import BASE_URL, HEADERS, TEAM_ID

payload = {
        "team_id": TEAM_ID,
        "name": "unique-autotest-channel",
        "display_name": "Unique AutoTest Channel",
        "type": "O"
    }

def test_create_channel():
    r = requests.post(f"{BASE_URL}/channels", headers=HEADERS, json=payload)
    assert r.status_code == 201

def test_create_channel_with_existing_name():
    r = requests.post(f"{BASE_URL}/channels", headers=HEADERS, json=payload)
    assert r.status_code == 400