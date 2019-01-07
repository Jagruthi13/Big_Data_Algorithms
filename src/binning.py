import numpy as np
import copy


def create_bins(data, bin_size):
    bins = dict()
    data = np.array(data)
    data = np.sort(data)

    split_array = np.split(data, range(0, len(data), bin_size))

    for idx in range(1, len(split_array)):
        bins[idx] = split_array[idx]

    return copy.deepcopy(bins)


def by_means(data, bin_size):
    bins_mean = create_bins(data, bin_size)

    for sub_bin in bins_mean.values():
        mean = np.floor(np.mean(sub_bin))
        sub_bin.fill(mean)

    return bins_mean


def by_boundaries(data, bin_size):
    bins_boundary = create_bins(data, bin_size)

    for sub_bin in bins_boundary.values():
        low = sub_bin[0]
        high = sub_bin[-1]
        for idx in range(len(sub_bin)):
            sub_bin[idx] = low if ((high - sub_bin[idx]) >= (sub_bin[idx] - low)) else high

    return bins_boundary


if __name__ == '__main__':
    size = 4
    list_sequence = [37, 30, 28, 13, 7, 3, 22, 8, 22, 22, 26, 26]

    print("binning: ", by_means(data=list_sequence, bin_size=size))
    print("binning: ", by_boundaries(data=list_sequence, bin_size=size))
