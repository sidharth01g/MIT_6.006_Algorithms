import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(1, parent_dir)

import Classes.adjacency_lists
test_adjacency_dict_0 = {"A": ["B", "C"],
                              "B": ["D"],
                              "C": ["D"],
                              "D": ["E"],
                              "E": []}

self.test_graph = Classes.adjacency_lists.TestGraph(
    self.test_adjacency_dict_0)
