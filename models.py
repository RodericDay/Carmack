from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase(':memory:', threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db

class Vehicle(BaseModel):
    brand = CharField()
    description = CharField()

db.connect()
db.create_tables([Vehicle])
