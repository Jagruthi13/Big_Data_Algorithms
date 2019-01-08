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


def by_ms(data, bin_size, type):
    bins_ms = create_bins(data, bin_size)

    if type is "mean":
        for sub_bin in bins_ms.values():
            mean = np.floor(np.mean(sub_bin))
            sub_bin.fill(mean)
    elif type is "median":
        for sub_bin in bins_ms.values():
            mean = np.floor(np.median(sub_bin))
            sub_bin.fill(mean)
    else:
        return bins_ms

    return bins_ms


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

    print("binning: ", by_ms(data=list_sequence, bin_size=size, type="mean"))
    print("binning: ", by_boundaries(data=list_sequence, bin_size=size))
