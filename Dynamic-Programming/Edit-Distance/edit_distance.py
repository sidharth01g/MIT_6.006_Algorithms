from collections import defaultdict
import math


class EditDistance():
    def __init__(self):
        self.min_distance_memo = None
        self.first_word = None
        self.second_word = None
        self.operations_stack = None

    def set_words(self, first_word, second_word):
        if type(first_word) is not str or type(second_word) is not str:
            print("ERROR: Argument not a string")
            return False
        self.first_word = first_word
        self.second_word = second_word
        self.min_distance_memo = defaultdict(dict)
        self.operations_stack = []

    def cost_insert(self, first_char, second_char):
        if type(first_char) is not str or type(second_char) is not str:
            print("ERROR: Argument not a string")
            return None
        if len(first_char) != 1 or len(second_char) !=1:
            print("ERROR: Argument not a single character")
            return None

        return 2

    def cost_delete(self, character):
        if type(character) is not str:
            print("ERROR: Argument not a string")
            return None
        if len(character) != 1:
            print("ERROR: Argument not a single character")
            return None

        return 1

    def cost_replace(self, first_char, second_char):
        if type(first_char) is not str or type(second_char) is not str:
            print("ERROR: Argument not a string")
            return None
        if len(first_char) != 1 or len(second_char) !=1:
            print("ERROR: Argument not a single character")
            return None
        if first_char == second_char:
            return 0
        else:
            return 3

    def min_dist(self, start_index_first, start_index_second):

        try:
            return self.min_distance_memo[start_index_first][start_index_second]
        except KeyError:
            pass

        print(self.first_word, ', ', self.second_word)
        print(start_index_first, ', ', start_index_second)

        # Base case
        if start_index_first >= len(self.first_word):
            cost = sum(self.cost_delete(character) for character in self.second_word[start_index_second:])
            return cost

        if start_index_second >= len(self.second_word):
            cost = sum(self.cost_delete(character) for character in self.first_word[start_index_first:])
            return cost

        #min_distance_value = min(
        cost_ins = (
            self.cost_insert(self.first_word[start_index_first],
                              self.second_word[start_index_second]) +
            self.min_dist(start_index_first,
                          start_index_second + 1)
        )
        cost_del = (
            self.cost_delete(self.first_word[start_index_first]) +
            self.min_dist(start_index_first + 1,
                          start_index_second)
        )
        cost_rep = (
            self.cost_replace(self.first_word[start_index_first],
                             self.second_word[start_index_second]) +
            self.min_dist(start_index_first + 1,
                          start_index_second + 1)
        )
        values = [cost_ins, cost_del, cost_rep]
        min_distance_value = min(values)
        print("-----> %s" % str(min_distance_value))
        self.min_distance_memo[start_index_first][start_index_second] = (
            min_distance_value)
        return min_distance_value

def main():
    distance_obj = EditDistance()
    distance_obj.set_words("abcdaskldjfl", "abcdakldjfl")
    min_distance_value = distance_obj.min_dist(0, 0)
    print("Memo:\n %s" % str(distance_obj.min_distance_memo))

    print("\nMin distance between '%s' and '%s': %s" % (
        distance_obj.first_word, distance_obj.second_word,
        min_distance_value))


if __name__ == '__main__':
    main()
