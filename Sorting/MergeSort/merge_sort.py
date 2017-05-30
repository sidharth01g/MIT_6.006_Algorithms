def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    middle = len(my_list) / 2
    sorted_left_list = merge_sort(my_list[0: middle])
    sorted_right_list = merge_sort(my_list[middle:])

    p = 0
    q = 0

    sorted_list = []
    while p < len(sorted_left_list) and q < len(sorted_right_list):
        if sorted_left_list[p] < sorted_right_list[q]:
            sorted_list.append(sorted_left_list[p])
            p += 1
        else:
            sorted_list.append(sorted_right_list[q])
            q += 1

    sorted_list.extend(sorted_left_list[p:])
    sorted_list.extend(sorted_right_list[q:])

    return sorted_list

a = [2, 5, 4, 1, 3, 9, 1]
print merge_sort(a)
