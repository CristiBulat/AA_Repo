import random
from performance import PerformanceAnalyzer
from visualization import Visualizer


def main():
    """
    Main function to run the experiments and generate graphs.
    """
    # Set random seed for reproducibility
    random.seed(42)

    # Create performance analyzer
    analyzer = PerformanceAnalyzer()

    # Run experiments
    analyzer.run_experiments()

    # Display results
    analyzer.display_results()

    # Get results for visualization
    (
        graph_sizes,
        sparse_dijkstra_times, sparse_floyd_times,
        dense_dijkstra_times, dense_floyd_times,
        sparse_dijkstra_memory, sparse_floyd_memory,
        dense_dijkstra_memory, dense_floyd_memory
    ) = analyzer.get_results()

    # Generate plots
    Visualizer.plot_execution_time(
        graph_sizes,
        sparse_dijkstra_times, sparse_floyd_times,
        dense_dijkstra_times, dense_floyd_times
    )

    Visualizer.plot_memory_usage(
        graph_sizes,
        sparse_dijkstra_memory, sparse_floyd_memory,
        dense_dijkstra_memory, dense_floyd_memory
    )

    print("\nExperiment completed successfully!")


if __name__ == "__main__":
    main()