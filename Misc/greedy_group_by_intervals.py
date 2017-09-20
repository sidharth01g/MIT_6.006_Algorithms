# Uses numpy
import numpy as np


def get_groups(ages, interval):
    ages = list(ages)
    ages.sort()
    interval = float(interval)
    current = 0
    groups = []
    while current <= len(ages) - 1:
        low = ages[current]
        high = ages[current] + interval
        groups.append((low, high))

        while (current <= len(ages) - 1) and (ages[current] <= high):
            current += 1
    return groups


def main():
    interval = 5
    ages = np.random.uniform(1, 100, size=(200))
    print('Ages:\n', ages)
    print('\nInterval: ', interval)
    groups = get_groups(ages, interval)
    print('\nNumber of groups: ', len(groups))
    print('\nGroups:\n', groups)


if __name__ == '__main__':
    main()
