import requests, pytest
from config import BASE_URL, HEADERS, CHANNEL_ID, USER_ID

def test_add_user_to_channel():
    payload = {
        "user_id": USER_ID
        }
    r = requests.post(f"{BASE_URL}/channels/{CHANNEL_ID}/members", headers=HEADERS, json=payload)
    print(r.text)
    assert r.status_code == 201

def test_remove_user_from_channel():
    r = requests.delete(f"{BASE_URL}/channels/{CHANNEL_ID}/members/{USER_ID}", headers=HEADERS)
    assert r.status_code == 200