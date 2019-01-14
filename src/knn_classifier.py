import pandas as pd
from scipy.spatial import distance


def knn_classifier(path, target_classes, classifier, sample, k, type='euclidean'):
    training_set = pd.DataFrame(pd.read_csv(path))
    classes_set = training_set[target_classes]
    if type is 'euclidean':
        training_set['dist'] = [distance.euclidean(row, sample) for row in classes_set.values]
    elif type is 'minkowski':
        training_set['dist'] = [distance.minkowski(row, sample) for row in classes_set.values]
    training_set.sort_values('dist', inplace=True)
    return (training_set.iloc[:k][classifier]).value_counts().idxmax()


if __name__ == '__main__':
    pd.set_option('display.max_columns', 10)
    print(knn_classifier(path="../knn_training_set.csv",
                   target_classes=['mass', 'width', 'height'],
                   classifier='fruit_name',
                   sample=(300, 7, 10),
                   k=5, type='minkowski'))
