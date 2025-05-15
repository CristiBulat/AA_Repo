from collections import deque
from typing import List, Dict, Union


def dfs(adj: Union[List[List[int]], List[Dict[int, int]]], start: int):
    """
    Depth-First Search implementation with metrics tracking.

    Args:
        adj: Adjacency list or dictionary representation of the graph
        start: Starting vertex

    Returns:
        Dictionary with traversal metrics
    """
    visited = [False] * len(adj)
    stack = [start]
    metrics = {
        'vertices': 0,  # Count of visited vertices
        'edges': 0,  # Count of explored edges
        'memory': 0,  # Peak stack size
        'traversal': []  # Visit order
    }

    while stack:
        metrics['memory'] = max(metrics['memory'], len(stack))
        vertex = stack.pop()

        if not visited[vertex]:
            visited[vertex] = True
            metrics['vertices'] += 1
            metrics['traversal'].append(vertex)

            neighbors = adj[vertex].keys() if isinstance(adj[vertex], dict) else adj[vertex]
            for neighbor in reversed(list(neighbors)):
                metrics['edges'] += 1
                if not visited[neighbor]:
                    stack.append(neighbor)

    return metrics


def bfs(adj: Union[List[List[int]], List[Dict[int, int]]], start: int):
    """
    Breadth-First Search implementation with metrics tracking.

    Args:
        adj: Adjacency list or dictionary representation of the graph
        start: Starting vertex

    Returns:
        Dictionary with traversal metrics
    """
    visited = [False] * len(adj)
    queue = deque([start])
    visited[start] = True
    metrics = {
        'vertices': 0,
        'edges': 0,
        'memory': 0,
        'traversal': []
    }

    while queue:
        metrics['memory'] = max(metrics['memory'], len(queue))
        vertex = queue.popleft()
        metrics['vertices'] += 1
        metrics['traversal'].append(vertex)

        neighbors = adj[vertex].keys() if isinstance(adj[vertex], dict) else adj[vertex]
        for neighbor in neighbors:
            metrics['edges'] += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return metrics