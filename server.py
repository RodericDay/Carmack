import bottle

not_implemented_json = { "success": False, "error": "Not implemented" }

data = []

@bottle.post('/autos')
def create_entry():
    return not_implemented_json

@bottle.get('/autos')
def query_all():
    return { "success": True, "data": data }

@bottle.get('/autos/<auto_id>')
def retrieve_entry(auto_id):
    return not_implemented_json

@bottle.put('/autos/<auto_id>')
def update_entry(auto_id):
    return not_implemented_json

@bottle.delete('/autos/<auto_id>')
def delete_entry(auto_id):
    return not_implemented_json

bottle.run(host='localhost', port=8080, quiet=True)
