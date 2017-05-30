import math


class Parenthesization:

    def __init__(self):
        self.min_cost_matrix = None
        self.matrix_size_list = None
        self.cost_trace_list = None

    def cost(self, start_index, intermediate_index, stop_index):
        """
        Returns cost of multiplying matrices
        """
        cost = (
            self.matrix_size_list[start_index][0] *
            self.matrix_size_list[intermediate_index][1] *
            self.matrix_size_list[stop_index][1])

        return cost

    def set_matrix_size_list(self, matrix_size_list):
        self.matrix_size_list = matrix_size_list
        length = len(matrix_size_list)
        self.min_cost_matrix = [
            [None for y in range(length)] for x in range(length)]
        self.cost_trace_list = []

    def get_min_cost(self, start_index, stop_index):
        # print("Start: %s, Stop %s" % (start_index, stop_index))

        matrix_value = self.min_cost_matrix[start_index][stop_index]
        if matrix_value:
            return matrix_value

        min_cost = math.inf
        min_cost_inter_index = None

        # Base case
        if stop_index <= start_index + 1:
            min_cost = 0

        for inter_index in range(start_index + 1, stop_index):
            inter_cost = (
                self.get_min_cost(start_index, inter_index) +
                self.get_min_cost(inter_index + 1, stop_index) +
                self.cost(start_index, inter_index, stop_index))
            if inter_cost < min_cost:
                min_cost = inter_cost
                min_cost_inter_index = inter_index

        self.cost_trace_list.append((start_index, min_cost_inter_index,
                                     stop_index, min_cost))
        """
        print("Split(%(i)s, %(j)s, %(k)s ): %(k)s" % {'i': start_index,
                                                      'j': min_cost_inter_index,
                                                      'k': stop_index,
                                                      'l': min_cost})
        """
        return min_cost

    def show_parenthesized(self, start_index, stop_index, displayed_list=[]):
        """
        Poor perforamnce because of list being used to store 'cost_trace_list'
        Output not formatted correctly
        """
        message = '('
        if start_index not in displayed_list:
            message += str(start_index)
            if stop_index != start_index:
                message += '*'
            displayed_list.append(start_index)
        print(message, end='')
        #print(start_index, stop_index)
        for item in self.cost_trace_list:
            if item[0] == start_index and item[2] == stop_index and item[1]:
                self.show_parenthesized(start_index, item[1])
                self.show_parenthesized(item[1] + 1, stop_index)
                break

        message = ')'
        if stop_index not in displayed_list:
            message = str(stop_index) + message
            displayed_list.append(stop_index)
        print(message, end='')


def main():

    matrix_size_list = [(10, 50), (50, 12), (12, 29), (29, 100), (100, 1),
                        (1, 25), (25, 399), (399, 1000), (1000, 40)]

    paren = Parenthesization()
    paren.set_matrix_size_list(matrix_size_list)

    print("Matrix sizes:\n%s" % str(matrix_size_list))
    print("Minimum number of multiplications: %s" % str(
        paren.get_min_cost(0, len(matrix_size_list) - 1)))
    # print(paren.cost_trace_list)
    print("Parenthesization in minimized number of arithmetic multiplications:")
    paren.show_parenthesized(0, len(matrix_size_list) - 1)
    print("\n")


if __name__ == "__main__":
    main()
