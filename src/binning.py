import numpy as np
import copy


def by_means(data, bin_size):
    bins = dict()
    data = np.array(data)
    data = np.sort(data)

    split_array = np.split(data, range(0, len(data), bin_size))

    for idx in range(1, len(split_array)):
        bins[idx] = split_array[idx]

    bins_mean = copy.deepcopy(bins)

    for sub_bin in bins_mean.values():
        mean = np.floor(np.mean(sub_bin))
        sub_bin.fill(mean)
        
    return bins_mean


if __name__ == '__main__':
    size = 4
    list_sequence = [37, 30, 28, 13, 7, 3, 22, 8, 22, 22, 26, 26]

    print("binning: ", by_means(data=list_sequence, bin_size=size))
