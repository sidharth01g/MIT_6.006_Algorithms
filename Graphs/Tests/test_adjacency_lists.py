import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(1, parent_dir)

class TestAdjacencyLists:

    def setup(self):
        import Classes.adjacency_lists
        self.test_adjacency_dict_0 = {"A": ["B", "C"],
                                      "B": ["D"],
                                      "C": ["D"],
                                      "D": ["E"],
                                      "E": []}

        self.test_graph = Classes.adjacency_lists.TestGraph(
            self.test_adjacency_dict_0)

    def teardown(self):
        pass

    def test_case_1(self):
        import Classes.adjacency_lists
        assert isinstance(self.test_graph, Classes.adjacency_lists.TestGraph)

    def test_case_2(self):
        import Classes.adjacency_lists
        print self.test_graph.__dict__
        assert (type(self.test_graph.adjacency_dict) is dict)

    def test_case_3(self):
        import Classes.adjacency_lists
        assert cmp(self.test_adjacency_dict_0.keys(),
                   self.test_graph.get_vertices()) == 0

    def test_bfs(self):
        import Classes.adjacency_lists
        print self.test_graph.breadth_first_search("A")
        assert False

    def test_dfs(self):
        import Classes.adjacency_lists
        print self.test_graph.depth_first_search()
        assert False

    def test_topological_sort(self):
        import Classes.adjacency_lists
        print self.test_graph.topological_sort()
        assert False
