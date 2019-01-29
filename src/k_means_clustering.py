import pandas as pd
import numpy as np
import plotly.offline as plt
import plotly.graph_objs as go
import sys

pd.set_option('display.max_columns', 10)


def k_means_clustering(path, k):
    data = pd.read_csv(path)
    data = data[['V1','V2']]
    k_means = (data.sample(k, replace=False))
    k_means2 = pd.DataFrame()
    clusters = pd.DataFrame()
    print('Initial means:\n', k_means)

    while not k_means2.equals(k_means):

        # distance matrix
        cluster_count = 0
        for idx, k_mean in k_means.iterrows():
            clusters[cluster_count] = (data[k_means.columns] - np.array(k_mean)).pow(2).sum(1).pow(0.5)
            cluster_count += 1

        # update cluster
        data['MDCluster'] = clusters.idxmin(axis=1)

        # store previous cluster
        k_means2 = k_means
        k_means = pd.DataFrame()
        k_means_frame = data.groupby('MDCluster').agg(np.mean)

        k_means[k_means_frame.columns] = k_means_frame[k_means_frame.columns]

        print(k_means.equals(k_means2))

    # plotting
    print('Plotting...')
    data_graph = [go.Scatter(
        x=data['V1'],
        y=data['V2'].where(data['MDCluster'] == c),
        mode='markers',
        name='Cluster: ' + str(c)
    ) for c in range(k)]

    plt.plot(data_graph, filename='Cluster.html')


if __name__ == '__main__':
    k_means_clustering(path='../datasets/knn_clustering_test_2.csv', k=4)
