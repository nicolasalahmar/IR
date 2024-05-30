import os

import peewee
from atpbar import atpbar
from dotenv import load_dotenv

from Offline.Helper.ORM import create_record, record_exists
from Offline.Pipeline.preprocessor.preprocessor import preprocessor

load_dotenv()


def insert_records(name, records):
    for i in atpbar(range(len(records)), name=name):
        if not record_exists(records[i], model=os.getenv('new_model')):
            records[i].text = preprocessor(records[i].text)
            try:
                create_record(records[i], model=os.getenv('new_model'))
            except peewee.OperationalError:
                create_record(records[i], model=os.getenv('new_model'))


def add_to_queue(records1, queue):
    for i, rec in enumerate(records1):
        name = 'task {}'.format(i)
        queue.put((name, rec))


def split_arr(records, n):
    try:
        length = len(records)
    except:
        records = list(records)
        length = len(list(records))

    chunk_size = int(length / n)
    return [records[i:i + chunk_size] for i in range(0, length, chunk_size)]
