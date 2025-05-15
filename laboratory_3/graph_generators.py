import random
from typing import List, Dict


class GraphGenerator:
    """
    Class providing methods to generate different types of graphs for analysis.
    """

    def generate_finite_graph(self, size: int) -> List[List[int]]:
        """
        Generate a random finite graph with limited edges per vertex.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            edges = random.sample(range(size), min(3, size))
            for j in edges:
                if j != i and j not in adj[i]:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj

    def generate_complete_graph(self, size: int) -> List[List[int]]:
        """
        Generate a complete graph where every vertex connects to all others.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            adj[i] = [j for j in range(size) if j != i]
        return adj

    def generate_tree_graph(self, size: int) -> List[List[int]]:
        """
        Generate a binary tree graph.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size:
                adj[i].append(left)
                adj[left].append(i)
            if right < size:
                adj[i].append(right)
                adj[right].append(i)
        return adj

    def generate_sparse_graph(self, size: int) -> List[List[int]]:
        """
        Generate a sparse graph with approximately 2 edges per vertex.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            for _ in range(2):  # Only 2 edges per vertex
                j = random.randint(0, size - 1)
                if j != i and j not in adj[i]:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj

    def generate_dense_graph(self, size: int) -> List[List[int]]:
        """
        Generate a dense graph with ~70% connectivity probability.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                if random.random() < 0.7:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj

    def generate_bipartite_graph(self, size: int) -> List[List[int]]:
        """
        Generate a bipartite graph with two disjoint vertex sets.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        group1 = range(0, size // 2)
        group2 = range(size // 2, size)
        adj = [[] for _ in range(size)]
        for i in group1:
            for j in group2:
                if random.random() < 0.3:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj

    def generate_cyclic_graph(self, size: int) -> List[List[int]]:
        """
        Generate a simple cyclic graph (ring).

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            adj[i].append((i + 1) % size)
            adj[(i + 1) % size].append(i)
        return adj

    def generate_acyclic_graph(self, size: int) -> List[List[int]]:
        """
        Generate a directed acyclic graph (DAG).

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                if random.random() < 0.2:
                    adj[i].append(j)  # Directed edge from i to j
        return adj

    def generate_multigraph(self, size: int) -> List[List[int]]:
        """
        Generate a multigraph with potential multiple edges between vertices.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for _ in range(size * 2):
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)
            if u != v:
                adj[u].append(v)
                adj[v].append(u)
        return adj

    def generate_pseudograph(self, size: int) -> List[List[int]]:
        """
        Generate a pseudograph with self-loops and multiple edges.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            adj[i].append(i)  # Self-loop
            for j in range(i + 1, size):
                if random.random() < 0.2:
                    adj[i].append(j)
                    adj[j].append(i)
        return adj

    def generate_regular_graph(self, size: int) -> List[List[int]]:
        """
        Generate a regular graph where each vertex has the same degree.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        degree = min(3, size - 1)
        adj = [[] for _ in range(size)]
        vertices = list(range(size)) * degree
        random.shuffle(vertices)
        while len(vertices) >= 2:
            u = vertices.pop()
            v = vertices.pop()
            if u != v and v not in adj[u] and len(adj[u]) < degree and len(adj[v]) < degree:
                adj[u].append(v)
                adj[v].append(u)
        return adj

    def generate_weighted_graph(self, size: int) -> List[Dict[int, int]]:
        """
        Generate a weighted graph with random weights on edges.

        Args:
            size: Number of vertices

        Returns:
            Adjacency dictionary representation of the graph
        """
        adj = [{} for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                if random.random() < 0.3:
                    weight = random.randint(1, 10)
                    adj[i][j] = weight
                    adj[j][i] = weight
        return adj

    def generate_directed_graph(self, size: int) -> List[List[int]]:
        """
        Generate a directed graph.

        Args:
            size: Number of vertices

        Returns:
            Adjacency list representation of the graph
        """
        adj = [[] for _ in range(size)]
        for i in range(size):
            for _ in range(2):
                j = random.randint(0, size - 1)
                if j != i and j not in adj[i]:
                    adj[i].append(j)
        return adj