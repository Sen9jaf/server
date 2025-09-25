import sys
import os

# Додаємо корінь проєкту (/app у контейнері) в sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_root():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, World!" in resp.data
