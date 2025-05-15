import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Visualizer:
    @staticmethod
    def plot_execution_times(graph_sizes, results, save_path=None):
        """
        Plot execution time comparison between Prim and Kruskal.

        Args:
            graph_sizes: List of graph sizes tested
            results: Benchmark results dictionary
            save_path: Optional path to save the figure
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Sparse graph execution times
        ax1.plot(graph_sizes, results['sparse']['prim']['time'], 'o-', label='Prim')
        ax1.plot(graph_sizes, results['sparse']['kruskal']['time'], 's-', label='Kruskal')
        ax1.set_title('Execution Time on Sparse Graphs')
        ax1.set_xlabel('Number of Vertices')
        ax1.set_ylabel('Time (seconds)')
        ax1.legend()
        ax1.grid(True)

        # Dense graph execution times
        ax2.plot(graph_sizes, results['dense']['prim']['time'], 'o-', label='Prim')
        ax2.plot(graph_sizes, results['dense']['kruskal']['time'], 's-', label='Kruskal')
        ax2.set_title('Execution Time on Dense Graphs')
        ax2.set_xlabel('Number of Vertices')
        ax2.set_ylabel('Time (seconds)')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        # Don't try to show the plot interactively if running in PyCharm
        # Only save to file instead
        try:
            plt.close()  # Close the figure to prevent memory leaks
        except:
            pass

    @staticmethod
    def plot_memory_usage(graph_sizes, results, save_path=None):
        """
        Plot memory usage comparison between Prim and Kruskal.

        Args:
            graph_sizes: List of graph sizes tested
            results: Benchmark results dictionary
            save_path: Optional path to save the figure
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Sparse graph memory usage
        ax1.plot(graph_sizes, results['sparse']['prim']['memory'], 'o-', label='Prim')
        ax1.plot(graph_sizes, results['sparse']['kruskal']['memory'], 's-', label='Kruskal')
        ax1.set_title('Memory Usage on Sparse Graphs')
        ax1.set_xlabel('Number of Vertices')
        ax1.set_ylabel('Memory (bytes)')
        ax1.legend()
        ax1.grid(True)

        # Dense graph memory usage
        ax2.plot(graph_sizes, results['dense']['prim']['memory'], 'o-', label='Prim')
        ax2.plot(graph_sizes, results['dense']['kruskal']['memory'], 's-', label='Kruskal')
        ax2.set_title('Memory Usage on Dense Graphs')
        ax2.set_xlabel('Number of Vertices')
        ax2.set_ylabel('Memory (bytes)')
        ax2.legend()
        ax2.grid(True)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        # Don't try to show the plot interactively if running in PyCharm
        # Only save to file instead
        try:
            plt.close()  # Close the figure to prevent memory leaks
        except:
            pass

    @staticmethod
    def create_results_table(graph_sizes, results):
        """
        Create tables for the benchmark results.

        Args:
            graph_sizes: List of graph sizes tested
            results: Benchmark results dictionary

        Returns:
            sparse_df, dense_df: Pandas DataFrames with formatted results
        """
        # Format data for sparse graphs
        sparse_data = []
        for i, size in enumerate(graph_sizes):
            sparse_data.append([
                size,
                f"{results['sparse']['prim']['time'][i]:.6f}",
                f"{results['sparse']['kruskal']['time'][i]:.6f}",
                f"{results['sparse']['prim']['memory'][i]:.0f}",
                f"{results['sparse']['kruskal']['memory'][i]:.0f}"
            ])

        # Format data for dense graphs
        dense_data = []
        for i, size in enumerate(graph_sizes):
            dense_data.append([
                size,
                f"{results['dense']['prim']['time'][i]:.6f}",
                f"{results['dense']['kruskal']['time'][i]:.6f}",
                f"{results['dense']['prim']['memory'][i]:.0f}",
                f"{results['dense']['kruskal']['memory'][i]:.0f}"
            ])

        # Create DataFrames
        columns = ['Graph Size', 'Prim Time (s)', 'Kruskal Time (s)', 'Prim Mem (B)', 'Kruskal Mem (B)']
        sparse_df = pd.DataFrame(sparse_data, columns=columns)
        dense_df = pd.DataFrame(dense_data, columns=columns)

        return sparse_df, dense_df