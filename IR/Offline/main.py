from dotenv import load_dotenv

from Clustering import cluster_index
from Helper.ORM import fetch_records
from Helper.timing import Timing
from Offline.Pipeline.Evaluation.eval import evaluate
from Offline.Pipeline.index.index import Index

load_dotenv()


def create_index_and_save():
    # fetching new records
    records = fetch_records(model='Corpus')
    documents = [rec.text for rec in records]
    index = Index(records)
    index.save()
    return index, documents


if __name__ == '__main__':
    with Timing('Creating Index...'):
        # index, documents = create_index_and_save()
        index = Index.load(
            model_name="Offline/Pipeline/index/Saved/Wiki/countries_dates/model369721.pickle",
            tfidf_name="Offline/Pipeline/index/Saved/Wiki/countries_dates/tfidf369721.pickle",
            keys_name="Offline/Pipeline/index/Saved/Wiki/countries_dates/keys369721.pickle")

    print(index.tfidf_matrix.shape[1])

    with Timing('Evaluating Documents...'):
        ev = evaluate(index,
                      rel=2,
                      qrels_path="Offline/Pipeline/Evaluation/Wiki/qrels_wiki",
                      queries_path="Offline/Pipeline/Evaluation/Wiki/queries.csv",
                      run_path="Offline/Pipeline/Evaluation/Wiki/run_wiki_countries_dates(2)",
                      create_run_file_bool=False)
        ev.update((x, y * 100) for x, y in ev.items())
        print(ev)

        # cluster_index(index)

        # top_documents = index.search('IRAQ')
        # for idx, score in top_documents:
        #     print(f"Document {idx}: Similarity Score {score}")
