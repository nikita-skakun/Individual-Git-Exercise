from collections import deque


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
            vertex: The vertex to be added.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Adds an edge between two vertices in the graph.

        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.

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
            vertex1: The first vertex.
            vertex2: The second vertex.

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
            vertex: The vertex to be removed.

        Returns:
            bool: True if the vertex was removed successfully, False otherwise.
        """
        if vertex in self.adjacency_list:
            for neighbour in self.adjacency_list[vertex]:
                self.adjacency_list[neighbour].remove(vertex)
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

    def dfs(self, start_vertex):
        """
        Performs depth-first search (DFS) traversal starting from the specified vertex.

        Args:
            start_vertex: The starting vertex for DFS traversal.

        Returns:
            list: A list of visited vertices in the order they were visited.
        """
        visited = []  # List to keep track of visited vertices

        def dfs_recursive(vertex):
            visited.append(vertex)  # Add the visited vertex to the list
            for neighbour in self.adjacency_list[vertex]:
                if neighbour not in visited:
                    dfs_recursive(neighbour)  # Recursively visit neighbouring vertices

        dfs_recursive(start_vertex)  # Start DFS traversal from the start vertex
        return visited

    def bfs(self, start_vertex):
        """
        Performs breadth-first search (BFS) traversal starting from the specified vertex.

        Args:
            start_vertex (hashable): The starting vertex for BFS traversal.

        Returns:
            list: A list of visited vertices in the order they were visited.
        """
        visited = []  # List to keep track of visited vertices
        queue = deque([start_vertex])  # Queue to store vertices for traversal

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the queue
            if vertex not in visited:
                visited.append(vertex)  # Add the visited vertex to the list
                # Enqueue neighboring vertices
                for neighbour in self.adjacency_list[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return visited


# Example usage:
if __name__ == "__main__":
    # Initializing the graph
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    
    # Adding edges in a circle
    assert graph.add_edge("B", "C") == True
    assert graph.add_edge("A", "B") == True
    assert graph.add_edge("C", "D") == True
    assert graph.add_edge("D", "E") == True
    assert graph.add_edge("E", "A") == True
    
    # Running the Depth-first Search
    print("Depth-First Search:")
    print(graph.dfs("A"))
    
    # Running the Breadth-first Search
    print("Breadth-First Search:")
    print(graph.bfs("A"))
    
    # Showing the Adjacency List 
    print("Adjacency List:")
    print(graph.get_adjacency_list())
    
    # Checking if the graph responds correctly to a removed edge
    assert graph.remove_edge("A", "B") == True
    print("Adjacency List after removing edge between A and B:")
    print(graph.get_adjacency_list())
    
    # Checking if the graph responds correctly to a removed vertex
    assert graph.remove_vertex("C") == True
    print("Adjacency List after removing vertex C:")
    print(graph.get_adjacency_list())
