# Python 3.5
import math


class Justifier:

    def __init__(self, page_width):
        if type(page_width) is not int:
            print("ERROR: page width not an integer")
        if page_width < 1:
            print("ERROR: page width less than 1")
        self.page_width = page_width
        self.min_badness_dict = {}
        self.words_list = None
        self.trace_dict = {}

    def set_words_list(self, words_list):
        if type(words_list) is not list:
            print("ERROR: Text must be a list of words")
            return False
        max_length = max(len(word) for word in words_list)
        if self.page_width < max_length:
            print("ERROR: Page width too low. Increase to at least " +
                  str(max_length))
            return False
        self.min_badness_dict = {}
        self.trace_dict = {}
        self.words_list = words_list
        return True

    def badness(self, start_index, stop_index):
        # Compute no. of characters in self.words_list[start_index: stop_index]
        width = sum(
            len(word) for word in self.words_list[start_index: stop_index + 1])
        # Add length of spaces(assume single space between words)
        width += stop_index - start_index

        if width > self.page_width:
            badness_value = math.inf
        else:
            badness_value = (self.page_width - width) ** 2

        return badness_value

    def get_min_badness(self, start_index):

        # Check memo. Return the badness value if found
        if start_index in self.min_badness_dict:
            return self.min_badness_dict[start_index]

        # Initialize minimum to infinity
        min_badness = math.inf
        min_badness_stop_index = -1

        # Base case for recursion
        if start_index == len(self.words_list):
            min_badness = 0
            min_badness_stop_index = len(self.words_list)

        # Recursive badness minimization
        for stop_index in range(start_index + 1, len(self.words_list) + 1):
            current_badness = (
                self.badness(start_index, stop_index - 1) +
                self.get_min_badness(stop_index))

            if current_badness < min_badness:
                min_badness = current_badness
                min_badness_stop_index = stop_index

        # Memoize the minimum badness value for line starting at start_index
        self.min_badness_dict[start_index] = min_badness

        # Trace dictionary to find minimum badness index trace
        self.trace_dict[start_index] = (min_badness_stop_index, min_badness)

        return min_badness


def main():
    page_width = 30
    justifier = Justifier(page_width)

    text = "The barn owl (Tyto alba) is the most widely distributed species of owl, and one of the most widespread of all birds. It is also referred to as the common barn owl, to distinguish it from other species in its family, Tytonidae, which forms one of the two main lineages of living owls, the other being the typical owls (Strigidae). The barn owl is found almost everywhere in the world except polar and desert regions, Asia north of the Himalayas, most of Indonesia, and some Pacific islands"
    words_list = text.split()

    # Set words list
    if not justifier.set_words_list(words_list):
        exit(1)

    print("Minimum badness: %s" % str(justifier.get_min_badness(0)))

    print("Trace dictionary:")
    for key, value in justifier.trace_dict.items():
        print(str(key) + ': ' + str(value))

    print("\nOriginal text:")
    print(text)

    print("\nJustified text (Page width = %s characters):" % str(page_width))
    if page_width >= 2:
        print('<' + '-' * (page_width -2) + '>')
    index = 0
    while True:
        if index >= len(justifier.words_list):
            break

        line_end_index = (justifier.trace_dict[index])[0]
        line = ' '.join(justifier.words_list[index: line_end_index])
        print(line + ' ' * (page_width - len(line)) + " - " + str(len(line)) +
              " characters")
        index = line_end_index
    if page_width >= 2:
        print('<' + '-' * (page_width -2) + '>')

if __name__ == "__main__":
    main()
