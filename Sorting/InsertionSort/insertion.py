def swap(my_list, index):
    print my_list
    temp = my_list[index]
    my_list[index] = my_list[index + 1]
    my_list[index + 1] = temp
    return my_list

def insertion_sort(my_list):
    if len(my_list) < 2:
        return my_list

    key = 1
    while key < len(my_list):

        start = key - 1
        while(start >= 0):
            if my_list[start] < my_list[start + 1]:
                my_list = swap(my_list, start)
            start -= 1
        key += 1
    return my_list

a = [2, 5, 4, 1, 3, 9, 1]
print insertion_sort(a)
