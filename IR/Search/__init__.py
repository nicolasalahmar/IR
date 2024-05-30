from Offline.Pipeline.index.index import Index


def get_index(chosen_dataset):
    prefix = f"Search/Indexes/{chosen_dataset}/Corpus/"
    model_name = prefix + "model369721.pickle"
    tfidf_name = prefix + "tfidf369721.pickle"
    keys_name = prefix + "keys369721.pickle"

    return model_name, tfidf_name, keys_name


# model_name, tfidf_name, keys_name = get_index('wiki')
wiki_index = Index.load(*get_index('wiki'))
# wiki_index = Index.load(model_name=model_name, tfidf_name=tfidf_name, keys_name=keys_name)
# model_name, tfidf_name, keys_name = get_index('antique')
# antique_index = Index.load(model_name=model_name, tfidf_name=tfidf_name, keys_name=keys_name)

indexes = {
    'wiki': wiki_index,
    # 'antique': antique_index
}