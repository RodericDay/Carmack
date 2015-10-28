import bottle
from peewee import IntegrityError, DoesNotExist
from models import Vehicle
import base64

#
# UTIL
#

def parse(obj):
    ''' turns object from peewee model to dict '''
    data = {
        "id": obj.id,
        "brand": obj.brand,
        "cylinder": obj.cylinder,
        "description": obj.description,
        "year": obj.year,
        "owner": obj.owner,
    }
    if obj.photo:
        # ideally we would have a cdn and this would be a pointer to that cdn,
        # handled client-side. however, base64 will do for now
        data['photo'] = "data:image/png;base64,"+base64.b64encode(obj.photo).decode()
    return data

def validate(request_forms):
    try:
       if 'year' in request_forms:
            assert 1900 < int(request_forms['year']) < 2050
    except (ValueError, KeyError, AssertionError):
        raise IntegrityError

#
# API
#

@bottle.get('/autos')
def query_all():
    data = [parse(v) for v in Vehicle.select()]
    return { "success": True, "data": data }

@bottle.post('/autos')
def create_entry():
    try:
        validate(bottle.request.forms)
        item = Vehicle.create(**bottle.request.forms)
        return { "success": True, "data": parse(item) }
    except IntegrityError as error:
        return { "success": False, "error": "Creation rejected." }

@bottle.get('/autos/<auto_id:int>')
def retrieve_entry(auto_id):
    data = parse(Vehicle.get(Vehicle.id == auto_id))
    return { "success": True, "data": data }

@bottle.put('/autos/<auto_id:int>')
def update_entry(auto_id):
    try:
        validate(bottle.request.forms)
    except IntegrityError:
        return { "success": False, "error": "Update rejected." }

    try:
        item = Vehicle.get(Vehicle.id == auto_id)
    except DoesNotExist:
        return { "success": False, "error": "Item not found." }

    for key, value in bottle.request.forms.items():
        setattr(item, key, value)
    photo = bottle.request.files.get('photo')
    if photo:
        item.photo = photo.file.read()
    item.save()
    return { "success": True, "data": parse(item) }

@bottle.delete('/autos/<auto_id:int>')
def delete_entry(auto_id):
    Vehicle.get(Vehicle.id == auto_id).delete_instance()
    return { "success": True }

#
# STATIC
#

@bottle.route('/')
def serve_html():
    return bottle.template("static/client.html")

@bottle.route('/static/<filename>')
def serve_static(filename):
    return bottle.static_file(filename, root="static")

bottle.run(host='localhost', port=8080, quiet=True, debug=True)
