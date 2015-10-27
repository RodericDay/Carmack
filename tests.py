import requests

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

    data = {"brand": "Ferrari", "description": "red"}
    resp = requests.post("http://localhost:8080/autos", data=data).json()
    assert resp['success'] and resp['data']['brand'] == "Ferrari"

    resp = requests.get("http://localhost:8080/autos/0").json()
    assert resp['success'] and resp['data']['description'] == 'red'

    data = {"description": "yellow"}
    resp = requests.put("http://localhost:8080/autos/0", data=data).json()
    assert resp['success'] and resp['data']['description'] == 'yellow'

    resp = requests.delete("http://localhost:8080/autos/0").json()
    assert resp['success']

    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

