class Knapsack(object):
    def __init__(self, size, items_list):
        if type(size) is not int:
            print("ERROR: size not an integer")
            return None
        if type(items_list) is not list:
            print("ERROR: items dictionary not a list")
            return None
        self.size = size
        self.items_list = items_list

        no_of_items = len(items_list)
        self.max_value_memo = [
            [None for j in range(size + 1)] for i in range(no_of_items)
        ]

    def max_value(self, item_index, current_capacity):
        # print(item_index, current_capacity)
        if self.max_value_memo[item_index][current_capacity]:
            return self.max_value_memo[item_index][current_capacity]

        # Base case:
        if item_index == len(self.items_list) - 1:
            if self.items_list[item_index][2] > current_capacity:
                max_value_base = 0
            else:
                max_value_base = max(
                    0,
                    self.items_list[item_index][1] + 0)
            self.max_value_memo[item_index][current_capacity] = max_value_base
            return max_value_base

        # General case:
        else:
            if self.items_list[item_index][2] >= current_capacity:
                # Drop current item
                max_value_general = self.max_value(item_index + 1,
                                                   current_capacity)
            else:
                max_value_drop_current = (
                    self.max_value(item_index + 1, current_capacity))
                max_value_pick_current = (
                    self.items_list[item_index][1] +
                    self.max_value(
                        item_index + 1,
                        current_capacity - self.items_list[item_index][2]))

                max_value_general = max(max_value_drop_current,
                                        max_value_pick_current)

            self.max_value_memo[item_index][current_capacity] = (
                max_value_general
            )
            return max_value_general


def main():
    knapsack_size = 5
    items_list = [
        ["Statue", 10, 4],
        ["Ball", 4, 2],
        ["Pen", 7, 3],
    ]

    print("Items:\n%s" % str(items_list))
    print("Backpack size: %s" % str(knapsack_size))

    my_backpack = Knapsack(knapsack_size, items_list)
    maximum_earnings = my_backpack.max_value(0, knapsack_size)

    print("\nMemo:")
    for j in range(my_backpack.size + 1):
        for i in range(len(my_backpack.items_list)):
            print(str(my_backpack.max_value_memo[i][j]) + " ", end="")
        print("\n")

    print("Maximum earnings: %s" % str(maximum_earnings))


if __name__ == "__main__":
    main()
