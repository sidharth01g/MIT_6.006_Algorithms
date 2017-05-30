def shell_sort(a):
    gap = int(len(a) / 2)
    while gap:
        print("Gap: %s" % (gap))
        for i in range(1, len(a)):
            j = i - gap
            temp = a[i]
            while j >= 0 and a[j] > temp:
                a[j + gap] = a[j]
                j -= gap
            a[j + gap] = temp
        gap /= 2
    return a


a = [2 ,5, 4, 1, 3, 9, 1]
print(a)
print(shell_sort(a))
