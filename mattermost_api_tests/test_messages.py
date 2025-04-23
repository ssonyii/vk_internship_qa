import requests, pytest
from config import BASE_URL, HEADERS, CHANNEL_ID

def test_send_message():
    post = {
        "channel_id": CHANNEL_ID,
        "message": "Hello from test!"
    }
    r = requests.post(f"{BASE_URL}/posts", headers=HEADERS, json=post)
    assert r.status_code == 201

def test_receive_messages():
    r = requests.get(f"{BASE_URL}/channels/{CHANNEL_ID}/posts", headers=HEADERS)
    assert r.status_code == 200
    assert "posts" in r.json()