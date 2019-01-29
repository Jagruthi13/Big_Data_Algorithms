import pandas as pd
import numpy as np
import plotly.offline as plt
import plotly.graph_objs as go


def knn_classifier(path, target_classes, classifier, sample, k):
    training_set = pd.DataFrame(pd.read_csv(path))
    classes_set = training_set[target_classes]

    data_graph = [go.Scatter3d(
        x=classes_set[target_classes[0]],
        y=classes_set[target_classes[2]],
        z=classes_set[target_classes[2]],
        mode='markers',
        marker=dict(
            color='#212121',
        ),
        name='Points from training set'
    ), go.Scatter3d(
        x=[sample[0]],
        y=[sample[1]],
        z=[sample[2]],
        mode='markers',
        marker=dict(
            size=10,
            color='#FFD600',
        ),
        name='New sample'
    )]

    plt.plot(data_graph, filename='../output_files/knn_classification.html')

    training_set['dist'] = (classes_set[target_classes] - np.array(sample)).pow(2).sum(1).pow(0.5)
    training_set.sort_values('dist', inplace=True)
    return (training_set.iloc[:k][classifier]).value_counts().idxmax()


if __name__ == '__main__':
    pd.set_option('display.max_columns', 10)
    print(knn_classifier(path="../datasets/knn_training_set.csv",
                         target_classes=['mass', 'width', 'height'],
                         classifier='fruit_name',
                         sample=[300, 7, 10],
                         k=5))
