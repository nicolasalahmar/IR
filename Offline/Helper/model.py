from peewee import *


# default database
db = SqliteDatabase('../dataset1.db')


class Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Corpus._meta.database = db

    class Meta:
        database = db
