import pandas as pd

frequency_table = None
prob_classes = None
c = None


def naive_bayes_classifier(data, class_name):
    global c, prob_classes, frequency_table
    c = data[class_name].value_counts()

    prob_classes = data[class_name].value_counts() / data[class_name].size

    features_cols = data.drop(class_name, axis=1).columns.values
    frequencies = [data.groupby([col, class_name]).size() for col in features_cols]

    frequency_table = pd.concat(frequencies, keys=features_cols)


def predict(features):
    temp_frequency_table = frequency_table.loc[:, features]

    class_pred = pd.Series(index=c.index)

    for idx in range(len(c.index)):
        temp_frequency_table.loc[:, :, c.index[idx]] = temp_frequency_table.loc[:, :, c.index[idx]] / c[idx]
        class_pred[c.index[idx]] = temp_frequency_table[:, :, c.index[idx]].product() * prob_classes[c.index[idx]]

    return class_pred.idxmax()


if __name__ == '__main__':
    data = pd.read_csv("../datasets/naive_bayes_training_set.csv")
    naive_bayes_classifier(data=data, class_name='buys_computer')
    print(
        predict(features=['<30', 'medium', 'yes', 'fair'])
    )
