def counting_sort(my_list):
    if any(type(x) is not int for x in my_list):
        raise TypeError("Non integer element in list")

    # Initialize to 0
    pos = [0 for x in range(max(my_list) + 1)]
    print(pos)

    # Generate element counts
    for element in my_list:
        pos[element] += 1
    # print(pos)

    k = len(pos)
    sum_ = sum(pos)

    # Generate starting positions
    for i in range(k - 1, -1, -1):
        sum_ -= pos[i]
        pos[i] = sum_

    # print(pos)

    # Generate output maintaining sortign stability
    out = [0 for x in range(len(my_list))]
    for element in my_list:
        out[pos[element]] = element
        pos[element] += 1
    return out


def main():
    my_array = [1, 4, 5, 2, 4, 2, 2, 7, 3, 1, 1, 1]
    print(counting_sort(my_array))


if __name__ == "__main__":
    main()
