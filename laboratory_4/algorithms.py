from typing import List, Dict, Tuple
import heapq


class ShortestPathAlgorithms:
    """
    Class containing implementations of shortest path algorithms.
    """

    @staticmethod
    def dijkstra(adj: List[Dict[int, int]], start: int) -> Dict[int, int]:
        """
        Dijkstra's algorithm for finding shortest paths from a source node.

        Args:
            adj: Adjacency list representation of the graph
            start: Source node

        Returns:
            Dictionary of shortest distances from the source to all nodes
        """
        dist = {i: float('inf') for i in range(len(adj))}
        dist[start] = 0
        visited = set()
        heap = [(0, start)]

        while heap:
            d, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)

            for v in adj[u]:
                if dist[u] + adj[u][v] < dist[v]:
                    dist[v] = dist[u] + adj[u][v]
                    heapq.heappush(heap, (dist[v], v))

        return dist

    @staticmethod
    def floyd_warshall(adj: List[Dict[int, int]]) -> List[List[float]]:
        """
        Floyd-Warshall algorithm for finding all-pairs shortest paths.

        Args:
            adj: Adjacency list representation of the graph

        Returns:
            Matrix of shortest distances between all pairs of nodes
        """
        size = len(adj)
        dist = [[float('inf')] * size for _ in range(size)]
        for i in range(size):
            dist[i][i] = 0
            for j in adj[i]:
                dist[i][j] = adj[i][j]

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist