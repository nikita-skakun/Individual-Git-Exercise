class Graph:
    """
    A class representing a graph using an adjacency list.
    """

    def __init__(self):
        """
        Initializes the graph with an empty adjacency list.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex (hashable): The vertex to be added.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Adds an edge between two vertices in the graph.

        Args:
            vertex1 (hashable): The first vertex.
            vertex2 (hashable): The second vertex.

        Returns:
            bool: True if the edge was added successfully, False otherwise.
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        """
        Removes an edge between two vertices in the graph.

        Args:
            vertex1 (hashable): The first vertex.
            vertex2 (hashable): The second vertex.

        Returns:
            bool: True if the edge was removed successfully, False otherwise.
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.

        Args:
            vertex (hashable): The vertex to be removed.

        Returns:
            bool: True if the vertex was removed successfully, False otherwise.
        """
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        else:
            return False

    def get_adjacency_list(self):
        """
        Returns the adjacency list representation of the graph.

        Returns:
            dict: The adjacency list representation of the graph.
        """
        return self.adjacency_list


# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.add_edge("A", "B") == True
    assert graph.add_edge("B", "C") == True
    assert graph.add_edge("A", "C") == True
    print("Adjacency List:")
    print(graph.get_adjacency_list())
    assert graph.remove_edge("A", "B") == True
    print("Adjacency List after removing edge between A and B:")
    print(graph.get_adjacency_list())
    assert graph.remove_vertex("C") == True
    print("Adjacency List after removing vertex C:")
    print(graph.get_adjacency_list())
