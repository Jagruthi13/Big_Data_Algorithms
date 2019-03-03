import numpy as np
from scipy import stats


def min_max(data, new_min, new_max):
    data = np.array(data)
    min_original = np.min(data)
    max_min_difference = np.max(data) - min_original
    new_max_min_difference = new_max - new_min
    return {v: np.round((((v - min_original) / max_min_difference) * new_max_min_difference + new_min), 3) for v in
            data}


def z_score(data):
    data = np.asarray(data)
    data_mean = data.mean()
    data_std = data.std()
    return (data - data_mean) / data_std


if __name__ == '__main__':
    print(min_max([8, 10, 15, 20], new_min=0, new_max=1))
    print(z_score([0.7972, 0.0767, 0.4383, 0.7866, 0.8091, 0.1954, 0.6307, 0.6599, 0.1065, 0.0508]))
