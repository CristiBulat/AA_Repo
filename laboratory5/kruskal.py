import time
import sys


def kruskal(graph):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree.

    Args:
        graph: Graph instance

    Returns:
        Tuple of (mst_edges, execution_time, memory_used)
    """
    # Start timing
    start_time = time.time()

    # Get all edges and sort them by weight
    edges = graph.get_edges()
    edges.sort(key=lambda x: x[2])

    # Initialize Union-Find data structures
    num_vertices = graph.num_vertices
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    # Functions for Union-Find operations
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])  # Path compression
        return parent[u]

    def union(u, v):
        root_u, root_v = find(u), find(v)

        if root_u != root_v:
            # Union by rank
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    # Build MST
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

            # Early termination when MST is complete
            if len(mst) == num_vertices - 1:
                break

    # End timing
    end_time = time.time()

    # Calculate memory usage
    memory_used = sys.getsizeof(mst) + sys.getsizeof(parent) + sys.getsizeof(rank) + sys.getsizeof(edges)

    return mst, total_weight, end_time - start_time, memory_used