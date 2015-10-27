from peewee import SqliteDatabase, Model, \
    CharField, IntegerField, DateField

db = SqliteDatabase(':memory:', threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db

class Vehicle(BaseModel):
    description = CharField()
    cylinder = IntegerField()
    brand = CharField()
    year = DateField(formats="%Y")
    owner = CharField()

db.connect()
db.create_tables([Vehicle])
