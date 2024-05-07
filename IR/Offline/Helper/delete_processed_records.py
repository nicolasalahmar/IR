from peewee import SqliteDatabase

from Helper.ORM import fetch_records
from Helper.model import Corpus

records = fetch_records('../intermediary_dataset/partially_processed_dataset1.db')

Corpus.set_db(SqliteDatabase('../dataset1.db'))
counter = 0
for record in records:
    Corpus.delete().where(Corpus.id == record.id).execute()
    counter += 1
    print(counter)
