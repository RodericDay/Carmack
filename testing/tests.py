import requests, json

def test_integration():
    data = {"brand": "Ferrari",
            "cylinder": 12,
            "description": "red",
            "year": 1993,
            "owner": "John Carmack"}
    resp = requests.post("http://localhost:8080/autos", data=data).json()
    assert resp['success'] and resp['data']['owner'] == "John Carmack"

    auto_id = str(resp['data']['id'])
    resp = requests.get("http://localhost:8080/autos/"+auto_id).json()
    assert resp['success'] and resp['data']['description'] == 'red'

    data = {"owner": "Dennis 'Thresh' Fong"}
    resp = requests.put("http://localhost:8080/autos/"+auto_id, data=data).json()
    assert resp['success'] and resp['data']['owner'] == "Dennis 'Thresh' Fong"

    resp = requests.delete("http://localhost:8080/autos/"+auto_id).json()
    assert resp['success']

    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == 0

def test_inadequate():
    resp = requests.post("http://localhost:8080/autos", data={'a': 'b'}).json()
    assert not resp['success'] and resp['error']

def test_populate_mock_data():
    with open('testing/mock_data.json') as fp:
        data = json.load(fp)

    for entry in data:
        resp = requests.post("http://localhost:8080/autos", data=entry).json()
        assert resp['success']

    resp = requests.get("http://localhost:8080/autos").json()
    assert resp['success'] and len(resp['data']) == len(data)

def test_store_photo():
    with open('testing/carmack.jpg', 'rb') as fp:
        files = {'photo': fp.read()}

    resp = requests.put("http://localhost:8080/autos/1", files=files).json()
    assert resp['success'] and resp['data']['photo']

def test_doesnt_validate():
    resp = requests.put("http://localhost:8080/autos/1", data={'year': 1800}).json()
    assert not resp['success']

def test_not_found():
    resp = requests.put("http://localhost:8080/autos/100", data={'year': 1999}).json()
