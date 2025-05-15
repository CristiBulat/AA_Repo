import matplotlib.pyplot as plt
from typing import List, Dict


def plot_results(sizes: List[int], dfs_metrics: List[Dict], bfs_metrics: List[Dict], graph_type: str) -> None:
    """
    Generate and save visualization plots for time and memory metrics.

    Args:
        sizes: List of graph sizes
        dfs_metrics: List of DFS performance metrics
        bfs_metrics: List of BFS performance metrics
        graph_type: Type of graph being analyzed
    """
    # Extract time and memory values
    dfs_times = [m['time'] for m in dfs_metrics]
    bfs_times = [m['time'] for m in bfs_metrics]
    dfs_memory = [m['traversal_memory'] for m in dfs_metrics]
    bfs_memory = [m['traversal_memory'] for m in bfs_metrics]

    # Create figure with two subplots
    plt.figure(figsize=(12, 5))

    # Time comparison plot
    plt.subplot(1, 2, 1)
    plt.plot(sizes, dfs_times, 'r-', marker='o', label='DFS')
    plt.plot(sizes, bfs_times, 'b-', marker='x', label='BFS')
    plt.xlabel('Graph Size (Vertices)')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Time Comparison: {graph_type}')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Memory comparison plot
    plt.subplot(1, 2, 2)
    plt.plot(sizes, dfs_memory, 'r--', marker='o', label='DFS')
    plt.plot(sizes, bfs_memory, 'b--', marker='x', label='BFS')
    plt.xlabel('Graph Size (Vertices)')
    plt.ylabel('Peak Memory Usage')
    plt.title(f'Memory Usage: {graph_type}')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'results/{graph_type}_performance.png', dpi=300)
    plt.close()


def generate_summary_plot(results: Dict, top_graph_types: List[str] = None) -> None:
    """
    Generate a summary plot comparing algorithm performance across different graph types.

    Args:
        results: Dictionary containing all performance results
        top_graph_types: List of graph types to include (if None, uses all)
    """
    if top_graph_types is None:
        top_graph_types = list(results.keys())

    # Create figure for summary plots
    plt.figure(figsize=(14, 8))

    # Time ratio (BFS/DFS) comparison
    plt.subplot(1, 2, 1)
    for graph_type in top_graph_types:
        sizes = results[graph_type]['sizes']
        dfs_times = [m['time'] for m in results[graph_type]['dfs']]
        bfs_times = [m['time'] for m in results[graph_type]['bfs']]
        time_ratios = [b / d if d > 0 else 1 for b, d in zip(bfs_times, dfs_times)]

        plt.plot(sizes, time_ratios, marker='o', label=graph_type)

    plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5)
    plt.xlabel('Graph Size (Vertices)')
    plt.ylabel('Time Ratio (BFS/DFS)')
    plt.title('BFS/DFS Time Ratio Across Graph Types')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Memory ratio (BFS/DFS) comparison
    plt.subplot(1, 2, 2)
    for graph_type in top_graph_types:
        sizes = results[graph_type]['sizes']
        dfs_memory = [m['traversal_memory'] for m in results[graph_type]['dfs']]
        bfs_memory = [m['traversal_memory'] for m in results[graph_type]['bfs']]
        memory_ratios = [b / d if d > 0 else 1 for b, d in zip(bfs_memory, dfs_memory)]

        plt.plot(sizes, memory_ratios, marker='o', label=graph_type)

    plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5)
    plt.xlabel('Graph Size (Vertices)')
    plt.ylabel('Memory Ratio (BFS/DFS)')
    plt.title('BFS/DFS Memory Ratio Across Graph Types')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    plt.tight_layout()
    plt.savefig('results/algorithm_comparison_summary.png', dpi=300)
    plt.close()