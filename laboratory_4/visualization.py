import matplotlib.pyplot as plt
from typing import List


class Visualizer:
    """
    Class for creating visualizations of algorithm performance.
    """

    @staticmethod
    def plot_execution_time(
            graph_sizes: List[int],
            sparse_dijkstra_times: List[float],
            sparse_floyd_times: List[float],
            dense_dijkstra_times: List[float],
            dense_floyd_times: List[float]
    ):
        """
        Plot execution time comparison.

        Args:
            graph_sizes: List of graph sizes used in experiments
            sparse_dijkstra_times: Dijkstra execution times for sparse graphs
            sparse_floyd_times: Floyd-Warshall execution times for sparse graphs
            dense_dijkstra_times: Dijkstra execution times for dense graphs
            dense_floyd_times: Floyd-Warshall execution times for dense graphs
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot sparse graph data
        ax.plot(graph_sizes, sparse_dijkstra_times, 'o-', label='Dijkstra (Sparse)', color='blue')
        ax.plot(graph_sizes, sparse_floyd_times, 's-', label='Floyd-Warshall (Sparse)', color='red')

        # Plot dense graph data
        ax.plot(graph_sizes, dense_dijkstra_times, '^-', label='Dijkstra (Dense)', color='green')
        ax.plot(graph_sizes, dense_floyd_times, 'D-', label='Floyd-Warshall (Dense)', color='purple')

        ax.set_xlabel('Graph Size (number of nodes)')
        ax.set_ylabel('Execution Time (seconds)')
        ax.set_title('Execution Time: Dijkstra vs. Floyd-Warshall')
        ax.legend()
        ax.grid(True)

        # Save the figure
        plt.savefig('lab4_execution_time.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("Execution time plot saved as 'lab4_execution_time.png'")

    @staticmethod
    def plot_memory_usage(
            graph_sizes: List[int],
            sparse_dijkstra_memory: List[int],
            sparse_floyd_memory: List[int],
            dense_dijkstra_memory: List[int],
            dense_floyd_memory: List[int]
    ):
        """
        Plot memory usage comparison.

        Args:
            graph_sizes: List of graph sizes used in experiments
            sparse_dijkstra_memory: Dijkstra memory usage for sparse graphs
            sparse_floyd_memory: Floyd-Warshall memory usage for sparse graphs
            dense_dijkstra_memory: Dijkstra memory usage for dense graphs
            dense_floyd_memory: Floyd-Warshall memory usage for dense graphs
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot sparse graph data
        ax.plot(graph_sizes, sparse_dijkstra_memory, 'o-', label='Dijkstra (Sparse)', color='blue')
        ax.plot(graph_sizes, sparse_floyd_memory, 's-', label='Floyd-Warshall (Sparse)', color='red')

        # Plot dense graph data
        ax.plot(graph_sizes, dense_dijkstra_memory, '^-', label='Dijkstra (Dense)', color='green')
        ax.plot(graph_sizes, dense_floyd_memory, 'D-', label='Floyd-Warshall (Dense)', color='purple')

        ax.set_xlabel('Graph Size (number of nodes)')
        ax.set_ylabel('Memory Usage (bytes)')
        ax.set_title('Memory Usage: Dijkstra vs. Floyd-Warshall')
        ax.legend()
        ax.grid(True)

        # Save the figure
        plt.savefig('lab4_memory_usage.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("Memory usage plot saved as 'lab4_memory_usage.png'")