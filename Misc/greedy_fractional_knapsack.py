def get_ratio(item):
    return item[1] / item[0]


def get_max_value(items, capacity):
    """Returns maximum value possible

    items: list of tuples [(weight_0, value_0), ... ,(weight_n, value_n)]
    capacity: float. Maxmium weigh the knapsack can take
    """
    assert type(items) is list
    capacity = float(capacity)
    items = sorted(items, key=get_ratio, reverse=True)
    print('Items sorted by value to weight ratio: ', items)

    i = 0
    max_value = 0
    while items[i][0] <= capacity:
        capacity -= items[i][0]
        max_value += items[i][1]
        i += 1

    if i < len(items) - 1:
        max_value += capacity * items[i][1] / items[i][0]
        capacity = 0

    return max_value


def main():
    items = [(3, 2), (5, 4), (4, 3), (2, 1)]
    capacity = 10
    print('Items: ', items)
    max_value = get_max_value(items, capacity)
    print('Max value: ', max_value)


if __name__ == '__main__':
    main()
