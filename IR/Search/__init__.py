from Offline.Pipeline.index.index import Index


def get_index(chosen_dataset):
    prefix = f"Search/Indexes/{chosen_dataset}/"
    model_name = prefix + "model.pickle"
    tfidf_name = prefix + "tfidf.pickle"
    keys_name = prefix + "keys.pickle"

    return model_name, tfidf_name, keys_name


wiki_index = Index.load(*get_index('wiki'))
antique_index = Index.load(*get_index('antique'))

indexes = {
    'wikir': wiki_index,
    'antique': antique_index
}

datasets = {
    'wikir': 'Offline/dataset2.db',
    'antique': 'Offline/dataset1.db',
}