import os
from atpbar import atpbar
from dotenv import load_dotenv
from Helper.ORM import processed_record_exists
from Helper.model import Processed_Corpus
from Pipeline.preprocessor.preprocessor import preprocessor

load_dotenv()


def insert_records(name, records):
    for i in atpbar(range(len(records)), name=name):
        if not processed_record_exists(os.getenv('dataset'), records[i]):
            records[i].text = preprocessor(records[i].text)
            Processed_Corpus.create(id=records[i].id, text=records[i].text)


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
