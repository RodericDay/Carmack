import requests

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

    data = {"message": "hello"}
    resp = requests.post("http://localhost:8080/autos", data=data).json()
    assert resp['success'] and len(resp['data']) == 1
    assert "hello" in resp['data'][0]['message']
