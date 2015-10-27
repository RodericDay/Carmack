from peewee import SqliteDatabase, Model, \
    CharField, IntegerField, DateField

db = SqliteDatabase(':memory:', threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db

class Vehicle(BaseModel):
    description = CharField(null=False)
    cylinder = IntegerField(null=False)
    brand = CharField(null=False)
    year = DateField(formats="%Y")
    owner = CharField(null=False)

db.connect()
db.create_tables([Vehicle])
