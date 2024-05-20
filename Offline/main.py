import os

from dotenv import load_dotenv

from Helper.ORM import fetch_records
from Helper.timing import Timing
from Pipeline.Evaluation.eval import evaluate
from Pipeline.index.index import Index

load_dotenv()


def create_index_and_save():
    # fetching new records
    records = fetch_records()
    documents = [rec.text for rec in records]
    index = Index(records)
    index.save()
    return index, documents


if __name__ == '__main__':
    with Timing('Creating Index...'):
        # index, documents = create_index_and_save()
        index = Index.load(model_name=os.getenv("saved_model_name"), tfidf_name=os.getenv("saved_tfidf_name"), keys_name=os.getenv("saved_keys_name"))

    # print(len(index.tfidf_matrix.toarray()))

    with Timing('Evaluating Documents...'):
        ev = evaluate(index, create_run_file_bool=True)
        print(ev)

        # top_documents = index.search('IRAQ')
        # for idx, score in top_documents:
        #     print(f"Document {idx}: Similarity Score {score}")
