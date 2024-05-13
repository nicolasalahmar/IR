import os
import sqlite3
from peewee import SqliteDatabase
from Helper.model import Corpus, Processed_Corpus
from dotenv import load_dotenv

load_dotenv()


def fetch_records(ds, limit=None):
    Processed_Corpus.set_db(SqliteDatabase(ds))
    if limit:
        return Processed_Corpus.select().limit(limit)
    else:
        return Processed_Corpus.select()


def create_table(name, ds):
    sqliteConnection = sqlite3.connect(ds)
    cursor = sqliteConnection.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()


def fetch_new_records(base_ds, new_ds, limit=None):
    Corpus.set_db(SqliteDatabase(new_ds))

    Corpus.set_db(SqliteDatabase(base_ds))
    if limit:
        return Corpus.select().limit(limit)
    else:
        return Corpus.select()


def insert_record(ds, rec):
    Corpus.set_db(SqliteDatabase(ds))
    return Corpus.create(id=rec.id, text=rec.text)


def bulk_insert_records(ds, recs):
    Corpus.set_db(SqliteDatabase(ds))
    return Corpus.bulk_create(recs)


# def delete_records(record, db):
#     Corpus.set_db(SqliteDatabase(db))
#     Corpus.delete().where(Corpus.id == record.id).execute()

def processed_record_exists(ds, record):
    Corpus.set_db(SqliteDatabase(ds))
    return Processed_Corpus.select().where(Processed_Corpus.id == record.id).exists()
