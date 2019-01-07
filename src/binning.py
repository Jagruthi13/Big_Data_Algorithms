import numpy as np
import copy

bins = dict()


def by_means():
    bins_mean = copy.deepcopy(bins)
    for bin in bins_mean.values():
        mean = np.floor(np.mean(bin))
        bin.fill(mean)
    return bins_mean


if __name__ == '__main__':
    bin_size = 4
    data = [37, 30, 28, 13, 7, 3, 22, 8, 22, 22, 26, 26]
    data = np.array(data)
    data = np.sort(data)
    split_array = np.split(data, range(0, len(data), bin_size))
    for idx in range(1, len(split_array)):
        bins[idx] = split_array[idx]

    print("original: ", bins)

    print("binning: ", by_means())
