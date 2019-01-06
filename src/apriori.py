from itertools import chain, combinations

support_count_dict = dict()
subsets = dict()
items_dict = dict()


def generate_subsets():
    for subset in chain(*map(lambda x: combinations(items_dict.keys(), x), range(1, len(items_dict.keys()) + 1))):
        if len(subset) not in subsets.keys():
            subsets[len(subset)] = set()
        (subsets[len(subset)]).add(subset)


def perform_apriori(data, support_count):
    sup_dict = dict()
    for value in data.values():
        for item in value:
            if item in items_dict.keys():
                items_dict[item] += 1
                if items_dict[item] >= support_count:
                    key = "(" + item + ")"
                    if key in sup_dict.keys():
                        sup_dict[key] += 1
                    else:
                        sup_dict[key] = items_dict[item]
            else:
                items_dict[item] = 1
    support_count_dict[1] = sup_dict

    generate_subsets()

    for total_items in range(2, len(subsets) + 1):
        for s in subsets[total_items]:
            scount = 0
            for items in data.values():
                if set(s).issubset(items):
                    scount += 1
            if scount >= support_count:
                if total_items not in support_count_dict:
                    support_count_dict[total_items] = dict()
                key = "(" + ", ".join(s) + ")"
                if str(s) in support_count_dict[total_items].keys():
                    (support_count_dict[total_items])[key].add({key: scount})
                    print()
                else:
                    (support_count_dict[total_items])[key] = scount

    for k, v in support_count_dict.items():
        print(k, v)


if __name__ == '__main__':
    sup_count = 2
    table = {
        't1': {'i1', 'i2', 'i5'},
        't2': {'i2', 'i4'},
        't3': {'i2', 'i3'},
        't4': {'i1', 'i2', 'i4'},
        't5': {'i1', 'i3'},
        't6': {'i2', 'i3'},
        't7': {'i1', 'i3'},
        't8': {'i1', 'i2', 'i3', 'i5'},
        't9': {'i1', 'i2', 'i3'},
    }
    perform_apriori(data=table, support_count=sup_count)
