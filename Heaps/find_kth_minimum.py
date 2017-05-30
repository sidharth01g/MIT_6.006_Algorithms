import heaps

class AugmentedMinHeap(heaps.MinHeap):
    


def main():
    heap_size = 20
    my_heap = heaps.MinHeap(heap_size)
    for number in [2, 6, 4, 1, 3, 0, 1, 4, 6, 5, 9, 6, 2, 9, 1, 6, 5]:
        my_heap.insert(number)
        print(my_heap.array_list)

    # print("Heap sort: %s" % str(my_heap.heap_sort()))

    k = 4

    frontier_min_heap = heaps.MinHeap(heap_size)

    frontier_min_heap.insert(my_heap.min())

    print(frontier_min_heap.array_list)

    for i in range(k):
        ith_minimum = frontier_min_heap.extract_min()
        print("min-%s: %s" % (str(i), ith_minimum))



if __name__ == "__main__":
    main()
