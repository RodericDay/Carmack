import requests

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

    data = {"message": "hello"}
    resp = requests.post("http://localhost:8080/autos", data=data).json()
    assert resp['success'] and len(resp['data']) == 1
    assert "hello" in resp['data'][0]['message']

    resp = requests.get("http://localhost:8080/autos/0").json()
    assert resp['success'] and "hello" in resp['data']['message']

    data = {"message": "goodbye"}
    resp = requests.put("http://localhost:8080/autos/0", data=data).json()
    assert resp['success'] and "goodbye" in resp['data']['message']

    resp = requests.delete("http://localhost:8080/autos/0").json()
    assert resp['success']

    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

