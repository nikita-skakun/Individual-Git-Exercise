import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from graph_representation import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("A", "C")

    def test_add_vertex(self):
        self.graph.add_vertex("D")
        self.assertIn("D", self.graph.get_adjacency_list())

    def test_add_edge(self):
        self.graph.add_vertex("D")
        self.graph.add_edge("B", "D")
        adjacency_list = self.graph.get_adjacency_list()
        self.assertIn("D", adjacency_list["B"])
        self.assertIn("B", adjacency_list["D"])

    def test_remove_edge(self):
        self.graph.remove_edge("A", "B")
        adjacency_list = self.graph.get_adjacency_list()
        self.assertNotIn("B", adjacency_list["A"])
        self.assertNotIn("A", adjacency_list["B"])

    def test_remove_vertex(self):
        self.graph.remove_vertex("C")
        self.assertNotIn("C", self.graph.get_adjacency_list())
        self.assertNotIn("C", self.graph.get_adjacency_list().get("A", []))
        self.assertNotIn("C", self.graph.get_adjacency_list().get("B", []))

    def test_get_adjacency_list(self):
        expected_adjacency_list = {"A": ["B", "C"], "B": ["A", "C"], "C": ["B", "A"]}
        self.assertEqual(self.graph.get_adjacency_list(), expected_adjacency_list)


class TestDfs(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_vertex("D")
        self.graph.add_vertex("E")
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        self.graph.add_edge("C", "D")
        self.graph.add_edge("D", "E")
        self.graph.add_edge("E", "A")

    def test_dfs(self):
        self.assertEqual(self.graph.dfs("A"), ["A", "B", "C", "D", "E"])
        self.assertEqual(self.graph.dfs("B"), ["B", "A", "E", "D", "C"])
        self.assertEqual(self.graph.dfs("C"), ["C", "B", "A", "E", "D"])
        self.assertEqual(self.graph.dfs("D"), ["D", "C", "B", "A", "E"])
        self.assertEqual(self.graph.dfs("E"), ["E", "D", "C", "B", "A"])


if __name__ == "__main__":
    unittest.main()
