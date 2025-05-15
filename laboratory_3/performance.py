import time
import psutil
from typing import Callable, Dict, Any, List, Union


def measure_performance(algorithm: Callable, graph: Union[List[List[int]], List[Dict[int, int]]], trials: int = 5) -> \
Dict[str, float]:
    """
    Measure the time and memory performance of a graph traversal algorithm.

    Args:
        algorithm: The algorithm function to measure (DFS or BFS)
        graph: The graph data structure to traverse
        trials: Number of trials to run for averaging

    Returns:
        Dictionary with performance metrics
    """
    times = []
    mem_usage = []

    for _ in range(trials):
        # Time measurement
        start = time.perf_counter()
        metrics = algorithm(graph, 0)  # Start from node 0
        elapsed = time.perf_counter() - start

        # Memory tracking (resident set size)
        process = psutil.Process()
        mem = process.memory_info().rss / 1024  # KB

        times.append(elapsed)
        mem_usage.append(mem)

    return {
        'time': sum(times) / trials,
        'memory': sum(mem_usage) / trials,
        'vertices': metrics['vertices'],
        'edges': metrics['edges'],
        'traversal_memory': metrics['memory']  # Peak stack/queue size during traversal
    }