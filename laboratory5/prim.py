import heapq
import time
import sys


def prim(graph, start=0):
    """
    Prim's algorithm to find the Minimum Spanning Tree.

    Args:
        graph: Graph instance
        start: Starting vertex

    Returns:
        Tuple of (mst_edges, execution_time, memory_used)
    """
    adj = graph.get_adjacency_list()
    num_vertices = graph.num_vertices

    # Initialize data structures
    mst = []  # List to store MST edges
    total_weight = 0
    visited = [False] * num_vertices
    min_heap = [(0, start, -1)]  # (weight, vertex, parent) format

    # Start timing
    start_time = time.time()

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight

        # Add edge to MST (except for the starting vertex)
        if parent != -1:
            mst.append((parent, u, weight))

        # Add all adjacent edges to the priority queue
        for v, edge_weight in adj[u].items():
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v, u))

    # End timing
    end_time = time.time()

    # Calculate memory usage
    memory_used = sys.getsizeof(mst) + sys.getsizeof(visited) + sys.getsizeof(min_heap)

    return mst, total_weight, end_time - start_time, memory_used