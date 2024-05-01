from peewee import SqliteDatabase

from Helper.model import Corpus


def fetch_records(ds, limit=None):
    Corpus.set_db(SqliteDatabase(ds))
    if limit:
        return Corpus.select().limit(limit)
    else:
        return Corpus.select()
