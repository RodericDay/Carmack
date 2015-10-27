import bottle

data = []

@bottle.post('/autos')
def create_entry():
    data.append(dict(bottle.request.forms))
    return { "success": True, "data": data }

@bottle.get('/autos')
def query_all():
    return { "success": True, "data": data }

@bottle.get('/autos/<auto_id:int>')
def retrieve_entry(auto_id):
    return { "success": True, "data": data[auto_id] }

@bottle.put('/autos/<auto_id:int>')
def update_entry(auto_id):
    data[auto_id].update(dict(bottle.request.forms))
    return { "success": True, "data": data[auto_id] }

@bottle.delete('/autos/<auto_id:int>')
def delete_entry(auto_id):
    del data[auto_id]
    return { "success": True }

bottle.run(host='localhost', port=8080, quiet=True)
