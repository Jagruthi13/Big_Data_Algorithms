import pandas as pd
import collections
import numpy as np


def naive_bayes_classifier(path, class_name, target):
    unique_attributes_values = dict()
    class_label_probabilities = dict()
    attributes_label_probabilities = dict()
    target_label = dict()
    training_set = pd.DataFrame(pd.read_csv(path))

    # get all attributes and it's unique values
    for attr in training_set.keys():
        unique_attributes_values[attr] = np.unique(training_set[attr].values)

    # generate unique values of class
    class_name_values = {class_name: unique_attributes_values.pop(class_name)}

    print("class_name_values: ", class_name_values)
    print("unique_attributes_values: ", unique_attributes_values)

    # get probabilities of class values
    class_label_probabilities = dict(collections.Counter(np.array(training_set[class_name])))
    for attr, count in class_label_probabilities.items():
        class_label_probabilities[attr] = [count, count / training_set[class_name].size]
    print(class_label_probabilities)

    # generating probabilities for other attributes
    for label in class_label_probabilities.keys():
        target_probability = 1
        for attr_key, attr_value in target.items():
            target_probability *= len(
                training_set[(training_set[attr_key] == attr_value) & (training_set[class_name] == label)]) / \
                                  (class_label_probabilities[label])[0]
        target_label[(target_probability * (class_label_probabilities[label])[1])] = label

    print(target_label[max(target_label.keys())])


if __name__ == '__main__':
    naive_bayes_classifier(path="../training_set.csv",
                           class_name="buys_computer",
                           target={'age': '>40', 'income': 'low', 'student': 'yes', 'credit_rating': 'excellent'})
