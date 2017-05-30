# Maxheap implementation
def insert(heap, data):
    """
    Insert data into heap
    """
    if type(heap) is not list:
        print("Error in insert(). Heap not a list")
        return None
    if type(data) not in (int, float, str):
        print("Error in insert(). Data not a calid type")
        return None
    heap.append(data)
    heap = swap_with_parents(heap)
    return heap


def swap_with_parents(heap):
    """
    Swap iteratively till maxheap condition is satisfied
    """
    if not heap:
        print("Error in swap_with_parents(). Heap empty")
        return None
    current_index = len(heap) - 1

    while True:
        print("Curr: %s" % current_index)
        if current_index == 0:
            return heap
        parent_index = int((current_index - 1) / 2)
        temp = current_index
        heap, current_index = swap(heap, current_index, parent_index)
        if current_index is None or heap is None:
            return None
        if current_index == temp:
            return heap


def swap(heap, a, b):
    if heap[a] > heap[b]:
        temp = heap[a]
        heap[a] = heap[b]
        heap[b] = temp
        return (heap, b)
    else:
        return(heap, a)


def main():
    heap0 = []
    while True:
        data = int(raw_input("Insert: "))
        if data == 0:
            break
        heap = insert(heap0, data)
        if not heap:
            print("Exiting")
            exit(1)
    print("Heap array: " + str(heap0))


if __name__ == "__main__":
    main()
