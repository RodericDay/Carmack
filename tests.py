import requests

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] == False and "Not implemented" in resp['error']
