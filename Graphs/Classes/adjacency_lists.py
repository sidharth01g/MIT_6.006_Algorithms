class TestGraph:
    # adjacency_dict = None

    def __init__(self, adjacency_dict):

        if type(adjacency_dict) is not dict:
            print("ERROR: Adjacency dict not a python dictionary")
            return None

        vertices = adjacency_dict.keys()

        for key, adjacent_vertices in adjacency_dict.iteritems():
            if any (vertex not in vertices for vertex in adjacent_vertices):
                print("ERROR: Adjacency dict has invalid entries")
                return None
        self.adjacency_dict = adjacency_dict

    @property
    def vertices(self):
        return self.adjacency_dict.keys()

    def get_vertices(self):
        return self.adjacency_dict.keys()

    def breadth_first_search(self, start_vertex):
        vertices_list = self.adjacency_dict.keys()
        print vertices_list
        if start_vertex not in vertices_list:
            print("Error: Starting vertex '%s' not in list of vetices" %\
                str(start_vertex))
            return None

        next_frontier = [start_vertex]
        index = -1
        parent = {start_vertex: None}
        level = {start_vertex: index + 1}

        while next_frontier:

            current_frontier = next_frontier
            next_frontier = []
            index += 1

            for current_vertex in current_frontier:
                for adjacent_vertex in self.adjacency_dict[current_vertex]:
                    if adjacent_vertex not in parent:
                        parent[adjacent_vertex] = current_vertex
                        level[adjacent_vertex] = index + 1
                        next_frontier.append(adjacent_vertex)
        return level

    def deep_visit(self, start_vertex, parent):

        for connected_vertex in self.adjacency_dict[start_vertex]:
            if connected_vertex not in parent:
                parent[connected_vertex] = start_vertex
                parent = self.deep_visit(connected_vertex, parent)
            else:
                continue

        return parent

    def depth_first_search(self):
        parent = {}

        for start_vertex in self.adjacency_dict.keys():
            if start_vertex not in parent:
                parent[start_vertex] = None
                parent = self.deep_visit(start_vertex, parent)

        return parent

    def deep_visit_topological_sort(self, start_vertex, parent, sorted_list):

        for connected_vertex in self.adjacency_dict[start_vertex]:
            if connected_vertex not in parent:
                parent[connected_vertex] = start_vertex
                (parent, sorted_list) = self.deep_visit_topological_sort(
                    connected_vertex, parent, sorted_list)
                sorted_list.insert(0, connected_vertex)

        return (parent, sorted_list)

    def topological_sort(self):
        """
        Performs topological sort
        """

        parent = {}
        sorted_list = []

        for start_vertex in self.adjacency_dict.keys():
            if start_vertex not in parent:
                parent[start_vertex] = None
                (parent, sorted_list) = self.deep_visit_topological_sort(
                    start_vertex, parent, sorted_list)
                sorted_list.insert(0, start_vertex)

        return (parent, sorted_list)
