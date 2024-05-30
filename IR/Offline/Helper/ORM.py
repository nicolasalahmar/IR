import os
import sqlite3

from dotenv import load_dotenv
from peewee import SqliteDatabase

from .model import class_for_name

load_dotenv()
ds = os.getenv('dataset')


def change_db(ds, model=os.getenv('model')):
    c = class_for_name(model)
    c.set_db(SqliteDatabase(ds))


def fetch_records(model=os.getenv('model'), limit=None):
    c = class_for_name(model)
    change_db(ds)
    if limit:
        return c.select().limit(limit)
    else:
        return c.select()


def create_table(name, ds=os.getenv('dataset')):
    sqliteConnection = sqlite3.connect(ds)
    cursor = sqliteConnection.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()


def record_exists(record, model=os.getenv('model')):
    c = class_for_name(model)
    change_db(ds)

    return c.select().where(c.id == record.id).exists()


def get_record(doc_id, model=os.getenv('model')):
    c = class_for_name(model)
    change_db(ds)

    return c.select().where(c.id == doc_id)[0]


def create_record(record, model=os.getenv('model')):
    c = class_for_name(model)
    change_db(ds)
    change_db(ds, model=os.getenv('new_model'))
    t = c.create(id=record.id, text=record.text)
