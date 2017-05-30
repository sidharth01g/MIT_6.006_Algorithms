import time
def insertion_sort(a):
    if len(a) < 2:
        return a
    for i in range(1, len(a)):
        j = i - 1
        temp = a[i]
        while(j >= 0 and a[j] > temp):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

    return a


a = [2 ,5, 4, 1, 3, 9, 1]
print(a)
print(insertion_sort(a))
