from typing import List, Dict
import random


class GraphGenerator:
    """
    Class for generating random graphs with specified properties.
    """

    @staticmethod
    def generate_graph(size: int, density: float) -> List[Dict[int, int]]:
        """
        Generate a random graph with specified size and density.

        Args:
            size: Number of nodes in the graph
            density: Edge density (probability of an edge between any two nodes)

        Returns:
            Adjacency list representation of the graph
        """
        adj = [{} for _ in range(size)]
        max_edges = size * (size - 1)  # Maximum possible edges in a directed graph
        target_edges = int(max_edges * density)

        edges_added = 0
        while edges_added < target_edges:
            # Select random source and destination nodes
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)

            # Avoid self-loops and duplicate edges
            if u != v and v not in adj[u]:
                # Add edge with random weight (1-10)
                weight = random.randint(1, 10)
                adj[u][v] = weight
                edges_added += 1

        return adj