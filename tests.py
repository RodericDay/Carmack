import requests, json

def test_integration():
    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

    data = {"brand": "Ferrari",
            "cylinder": 12,
            "description": "red",
            "year": 1993,
            "owner": "John Carmack"}
    resp = requests.post("http://localhost:8080/autos", data=data).json()
    assert resp['success'] and resp['data']['owner'] == "John Carmack"

    resp = requests.get("http://localhost:8080/autos/0").json()
    assert resp['success'] and resp['data']['description'] == 'red'

    data = {"owner": "Dennis 'Thresh' Fong"}
    resp = requests.put("http://localhost:8080/autos/0", data=data).json()
    assert resp['success'] and resp['data']['owner'] == "Dennis 'Thresh' Fong"

    resp = requests.delete("http://localhost:8080/autos/0").json()
    assert resp['success']

    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

def test_inadequate():
    resp = requests.post("http://localhost:8080/autos", data={'a': 'b'}).json()
    assert not resp['success'] and resp['error']

def test_populate_mock_data():
    with open('mock_data.json') as fp:
        data = json.load(fp)

    for entry in data:
        resp = requests.post("http://localhost:8080/autos", data=entry).json()
        assert resp['success']
