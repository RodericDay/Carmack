import bottle
from peewee import IntegrityError
from models import Vehicle

def parse(obj):
    ''' turns object from peewee model to dict '''
    return {
        "brand": obj.brand,
        "description": obj.description,
    }

@bottle.get('/autos')
def query_all():
    data = [parse(v) for v in Vehicle.select()]
    return { "success": True, "data": data }

@bottle.post('/autos')
def create_entry():
    try:
        data = parse(Vehicle.create(**bottle.request.forms))
        return { "success": True, "data": data }
    except IntegrityError as error:
        return { "success": False, "error": "Server rejected submission." }

@bottle.get('/autos/<auto_id:int>')
def retrieve_entry(auto_id):
    data = parse(Vehicle.select()[auto_id])
    return { "success": True, "data": data }

@bottle.put('/autos/<auto_id:int>')
def update_entry(auto_id):
    item = Vehicle.select()[auto_id]
    for key, value in bottle.request.forms.items():
        # peewee's update command is behaving strangely,
        # so update fields manually
        setattr(item, key, value)
    item.save()
    return { "success": True, "data": parse(item) }

@bottle.delete('/autos/<auto_id:int>')
def delete_entry(auto_id):
    Vehicle.select()[auto_id].delete_instance()
    return { "success": True }

@bottle.route('/')
def serve_html():
    return bottle.template("client.html")

@bottle.route('/static/<filename>')
def serve_static(filename):
    return bottle.static_file(filename, root="static")

bottle.run(host='localhost', port=8080, quiet=True, debug=True)
