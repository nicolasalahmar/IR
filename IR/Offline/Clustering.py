import pickle

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score


def find_optimal_clusters(data, max_k):
    iters = range(2, max_k + 1, 2)

    sse = []
    for k in iters:
        sse.append(MiniBatchKMeans(n_clusters=k, init_size=400000, batch_size=800000, random_state=20).fit(data).inertia_)
        print('Fit {} clusters'.format(k))

    pickle.dump(sse, open('sse.pickle', 'wb'))

    f, ax = plt.subplots(1, 1)
    ax.plot(iters, sse, marker='o')
    ax.set_xlabel('Cluster Centers')
    ax.set_xticks(iters)
    ax.set_xticklabels(iters)
    ax.set_ylabel('SSE')
    ax.set_title('SSE by Cluster Center Plot')

    plt.savefig('optimal.png')
    plt.show()


def plot_data(index, n_clusters=4, init_size=400000, batch_size=800000,  random_state=20):
    pca = PCA(n_components=2, svd_solver='arpack')
    reduced_data = pca.fit_transform(index.tfidf_matrix)

    kmeans = MiniBatchKMeans(n_clusters=n_clusters, init_size=init_size, batch_size=batch_size, random_state=random_state)
    clusters = kmeans.fit_predict(reduced_data)

    max_label = max(clusters)

    idx = np.random.choice(range(reduced_data.shape[0]), size=300, replace=False)
    label_subset = clusters[idx]
    label_subset = [cm.hsv(i / max_label) for i in label_subset]

    f, ax = plt.subplots(1, 1, figsize=(7, 7))

    ax.scatter(reduced_data[idx, 0], reduced_data[idx, 1], c=label_subset)
    ax.set_title('PCA Cluster Plot')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')

    plt.savefig('clusters.png')
    # plt.show()

    return reduced_data, clusters


def cluster_index(index, n_clusters=4, init_size=400000, batch_size=800000,  random_state=20):
    # Display Curve to find Elbow point
    # find_optimal_clusters(index.tfidf_matrix, 20)

    reduced_data, clusters = plot_data(index, n_clusters=n_clusters, init_size=init_size, batch_size=batch_size,  random_state=random_state)
    silhouette_avg = silhouette_score(reduced_data, clusters)
    print("Silhouette Score: ", silhouette_avg)
