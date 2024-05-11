from peewee import SqliteDatabase
import os
from dotenv import load_dotenv
from Helper.ORM import fetch_records
from Helper.model import Corpus

load_dotenv()

records = fetch_records('../intermediary_dataset/' + os.getenv('partially_processed_db'))

Corpus.set_db(SqliteDatabase('../' + os.getenv('dataset')))
counter = 0
for record in records:
    Corpus.delete().where(Corpus.id == record.id).execute()
    counter += 1
    print(counter)
