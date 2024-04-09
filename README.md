# Graph Implementation in Python

This Python module provides a basic implementation of a graph using an adjacency list representation. It includes functionalities to add vertices, add edges between vertices, remove edges, remove vertices, perform depth-first search (DFS) traversal, and breadth-first search (BFS) traversal.

## Features

- **Graph Representation**: The graph is represented using an adjacency list, which is a dictionary where each vertex is mapped to a list of its neighboring vertices.
- **Add and Remove Vertices**: The `add_vertex` method adds a vertex to the graph, while the `remove_vertex` method removes a vertex and its associated edges from the graph.
- **Add and Remove Edges**: The `add_edge` method adds an undirected edge between two vertices, while the `remove_edge` method removes an edge between two vertices.
- **Depth-First Search (DFS)**: The `dfs` method performs a depth-first search traversal starting from a specified vertex.
- **Breadth-First Search (BFS)**: The `bfs` method performs a breadth-first search traversal starting from a specified vertex.

## Usage

To use the `Graph` class, follow these steps:

1. Import the `Graph` class into your Python code.
2. Create an instance of the `Graph` class.
3. Use the various methods of the `Graph` class to perform operations such as adding vertices, adding edges, and traversing the graph using DFS or BFS.

Example usage:

```python
# Create a graph instance
graph = Graph()

# Add vertices to the graph
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

# Add edges between vertices
graph.add_edge("A", "B")
graph.add_edge("B", "C")

# Perform DFS traversal starting from vertex 'A'
print("Depth-First Search:")
print(graph.dfs("A"))

# Perform BFS traversal starting from vertex 'A'
print("Breadth-First Search:")
print(graph.bfs("A"))

# Get the adjacency list representation of the graph
print("Adjacency List:")
print(graph.get_adjacency_list())

# Remove an edge between vertices 'A' and 'B'
graph.remove_edge("A", "B")

# Remove vertex 'C' from the graph
graph.remove_vertex("C")
```

## Requirements

This code requires Python 3.x.

## License

This project is licensed under the MIT License.
