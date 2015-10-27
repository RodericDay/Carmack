import requests

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] == True and len(resp['data']) == 0
