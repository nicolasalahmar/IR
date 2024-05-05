from peewee import SqliteDatabase

from Helper.model import Corpus


def fetch_records(ds, limit=None):
    Corpus.set_db(SqliteDatabase(ds))
    if limit:
        return Corpus.select().limit(limit)
    else:
        return Corpus.select()


def fetch_new_records(base_ds, new_ds, limit=None):
    Corpus.set_db(SqliteDatabase(new_ds))
    new_recs = Corpus.select()
    keys = [x.id for x in new_recs]

    Corpus.set_db(SqliteDatabase(base_ds))
    if limit:
        return Corpus.select().where(~Corpus.id.in_(keys)).limit(limit)
    else:
        return Corpus.select().where(~Corpus.id.in_(keys))


def insert_record(ds, rec):
    Corpus.set_db(SqliteDatabase(ds))
    return Corpus.create(id=rec.id, text=rec.text)


def bulk_insert_records(ds, recs):
    Corpus.set_db(SqliteDatabase(ds))
    return Corpus.bulk_create(recs)
