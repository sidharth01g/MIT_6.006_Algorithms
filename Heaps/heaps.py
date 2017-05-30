class MinHeap(object):
    def __init__(self, array_size):
        if array_size < 1:
            print("ERROR: Cannot create heap of size less than 1")
        self.array_size = array_size
        self.array_list = [None for i in range(array_size)]
        self.last_index = -1

    def parent_index(self, index):
        return int((index - 1) / 2)

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def swap(self, first_index, second_index):
        temp = self.array_list[first_index]
        self.array_list[first_index] = self.array_list[second_index]
        self.array_list[second_index] = temp
        print("Swapped %s with %s" % (first_index, second_index))
        return True

    def swap_upwards(self, start_index):
        if start_index >= self.array_size:
            print("ERROR: Swap start index too large")
            return None
        if start_index <= 0:
            return True
        current_index = start_index
        parent_index = self.parent_index(current_index)
        if (self.array_list[current_index] < self.array_list[parent_index]):
            self.swap(current_index, parent_index)
            return self.swap_upwards(parent_index)
        else:
            return True

    def swap_downwards(self, start_index):
        print(self.array_list, self.last_index)
        print("Swap down from %s" % str(start_index))
        if start_index < 0:
            print("ERROR: Swap start index less than zero")
            return None

        current_index = start_index
        index_left_child = self.left_child_index(current_index)
        index_right_child = self.right_child_index(current_index)

        if index_left_child <= self.last_index and index_right_child > self.last_index:
            if self.array_list[current_index] > self.array_list[index_left_child]:
                self.swap(current_index, index_left_child)
                return self.swap_downwards(index_left_child)
            else:
                return True

        elif index_right_child <= self.last_index and index_left_child > self.last_index:
            if self.array_list[current_index] > self.array_list[index_right_child]:
                self.swap(current_index, index_right_child)
                return self.swap_downwards(index_right_child)
            else:
                return True

        elif index_left_child <= self.last_index and index_right_child <= self.last_index:
            # Identify the greater child!
            print((index_left_child, index_right_child))
            if self.array_list[index_left_child] < self.array_list[index_right_child]:
                lesser_child_index = index_left_child
            else:
                lesser_child_index = index_right_child
            if self.array_list[current_index] > self.array_list[lesser_child_index]:
                self.swap(current_index, lesser_child_index)
                return self.swap_downwards(lesser_child_index)
            else:
                return True
        else:
            # No children
            return True


    def insert(self, data):
        print("\nInsert: %s" % str(data))
        if self.last_index >= self.array_size - 1:
            print("ERROR: Array is full!")
            return False

        self.array_list[self.last_index + 1] = data
        self.last_index += 1
        return self.swap_upwards(self.last_index)

    def delete(self, data):
        print("\nDelete: %s" % str(data))
        try:
            index = self.array_list.index(data)
        except ValueError as error:
            print("ERROR: %s" % str(error))
            return False

        self.array_list[index] = self.array_list[self.last_index]
        self.array_list[self.last_index] = None
        self.last_index -= 1

        return self.swap_downwards(index)

    def min(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None
        return self.array_list[0]

    def extract_min(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None

        answer = self.array_list[0]
        self.array_list[0] = self.array_list[self.last_index]
        self.array_list[self.last_index] = None
        self.last_index -= 1
        self.swap_downwards(0)
        return answer

    def heap_sort(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None

        last_index_save = self.last_index

        while self.last_index >= 0:
            print("last_index: %s" % str(self.last_index))
            self.swap(0, self.last_index)
            self.last_index -= 1
            self.swap_downwards(0)

        return self.array_list[:last_index_save + 1]





class MaxHeap(object):
    def __init__(self, array_size):
        if array_size < 1:
            print("ERROR: Cannot create heap of size less than 1")
        self.array_size = array_size
        self.array_list = [None for i in range(array_size)]
        self.last_index = -1

    def parent_index(self, index):
        return int((index - 1) / 2)

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def swap(self, first_index, second_index):
        temp = self.array_list[first_index]
        self.array_list[first_index] = self.array_list[second_index]
        self.array_list[second_index] = temp
        print("Swapped %s with %s" % (first_index, second_index))
        return True

    def swap_upwards(self, start_index):
        if start_index >= self.array_size:
            print("ERROR: Swap start index too large")
            return None
        if start_index <= 0:
            return True
        current_index = start_index
        parent_index = self.parent_index(current_index)
        if (self.array_list[current_index] > self.array_list[parent_index]):
            self.swap(current_index, parent_index)
            return self.swap_upwards(parent_index)
        else:
            return True

    def swap_downwards(self, start_index):
        print(self.array_list, self.last_index)
        print("Swap down from %s" % str(start_index))
        if start_index < 0:
            print("ERROR: Swap start index less than zero")
            return None

        current_index = start_index
        index_left_child = self.left_child_index(current_index)
        index_right_child = self.right_child_index(current_index)

        if index_left_child <= self.last_index and index_right_child > self.last_index:
            if self.array_list[current_index] < self.array_list[index_left_child]:
                self.swap(current_index, index_left_child)
                return self.swap_downwards(index_left_child)
            else:
                return True

        elif index_right_child <= self.last_index and index_left_child > self.last_index:
            if self.array_list[current_index] < self.array_list[index_right_child]:
                self.swap(current_index, index_right_child)
                return self.swap_downwards(index_right_child)
            else:
                return True

        elif index_left_child <= self.last_index and index_right_child <= self.last_index:
            # Identify the greater child!
            print((index_left_child, index_right_child))
            if self.array_list[index_left_child] > self.array_list[index_right_child]:
                greater_child_index = index_left_child
            else:
                greater_child_index = index_right_child

            if self.array_list[current_index] < self.array_list[greater_child_index]:
                self.swap(current_index, greater_child_index)
                return self.swap_downwards(greater_child_index)
            else:
                return True
        else:
            # No children
            return True


    def insert(self, data):
        print("\nInsert: %s" % str(data))
        if self.last_index >= self.array_size - 1:
            print("ERROR: Array is full!")
            return False

        self.array_list[self.last_index + 1] = data
        self.last_index += 1
        return self.swap_upwards(self.last_index)

    def delete(self, data):
        print("\nDelete: %s" % str(data))
        try:
            index = self.array_list.index(data)
        except ValueError as error:
            print("ERROR: %s" % str(error))
            return False

        self.array_list[index] = self.array_list[self.last_index]
        self.array_list[self.last_index] = None
        self.last_index -= 1

        return self.swap_downwards(index)

    def max(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None
        return self.array_list[0]

    def extract_max(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None

        answer = self.array_list[0]
        self.array_list[0] = self.array_list[self.last_index]
        self.array_list[self.last_index] = None
        self.last_index -= 1
        self.swap_downwards(0)
        return answer

    def heap_sort(self):
        if self.last_index < 0:
            print("ERROR: Heap empty!")
            return None

        last_index_save = self.last_index

        while self.last_index >= 0:
            print("last_index: %s" % str(self.last_index))
            self.swap(0, self.last_index)
            self.last_index -= 1
            self.swap_downwards(0)

        return self.array_list[:last_index_save + 1]


def main():
    # my_heap = MaxHeap(20)
    my_heap = MinHeap(20)
    for number in [2, 6, 4, 1, 3, 0, 1, 4, 6, 5, 9, 6, 2, 9, 1, 6, 5]:
        my_heap.insert(number)
        print(my_heap.array_list)
    """
    print("*" * 100)
    my_heap.delete(9)

    print(my_heap.array_list)
    """
    """
    x = []
    while my_heap.last_index >= 0:
        x.append(my_heap.extract_max())
    print(x)
    """
    print("-" * 100)
    print("Heap sort: %s" % str(my_heap.heap_sort()))
    exit()
    for number in [2, 6, 4, 1, 3, 0, 1, 4, 6, 5, 9, 6, 2, 9, 1, 6, 5]:
        my_heap.delete(number)
        print(my_heap.array_list)

    print(my_heap.array_list)

if __name__ == "__main__":
    main()
