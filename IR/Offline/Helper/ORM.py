from peewee import SqliteDatabase

from Helper.model import Corpus


def fetch_records(ds, limit=None):
    Corpus.set_db(SqliteDatabase(ds))
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
