class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print('--------------------')
        for vertex in self.adj_list:
            print(vertex, ' : ', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass

            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


# adding a vertex
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
# g.print_graph()

# adding an edge
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')
g.print_graph()

# removing an edge
# g.remove_edge('A', 'B')
# g.print_graph()

# removing a vertex
g.remove_vertex('C')
g.print_graph()

