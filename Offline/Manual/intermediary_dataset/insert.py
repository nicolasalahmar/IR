import os
from dotenv import load_dotenv
from atpbar import atpbar
from Helper.ORM import bulk_insert_records, delete_records
import sqlite3
from Helper.model import Corpus
from Pipeline.preprocessor.preprocessor import preprocessor

load_dotenv()


def insert_records(name, records):
    for i in atpbar(range(len(records)), name=name):
        records[i].text = preprocessor(records[i].text)

    with Corpus._meta.database.atomic():
        bulk_insert_records(os.getenv('partially_processed_db'), records)
        for record in records:
            delete_records(record, os.getenv('dataset'))


def create_table():
    sqliteConnection = sqlite3.connect(os.getenv('partially_processed_db'))
    cursor = sqliteConnection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS corpus (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()


def split_arr(records1, n):
    chunk_size = int(len(records1) / n)
    return [records1[i:i + chunk_size] for i in range(0, len(records1), chunk_size)]
