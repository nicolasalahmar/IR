from peewee import *
import os
from dotenv import load_dotenv

load_dotenv()


# default database
db = SqliteDatabase(os.getenv('dataset'))


class Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Corpus._meta.database = db

    class Meta:
        database = db


class Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Corpus._meta.database = db

    class Meta:
        database = db
