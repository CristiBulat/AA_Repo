import os
from graph import Graph
from prim import prim
from kruskal import kruskal
from benchmark import Benchmark
from visualize import Visualizer


def verify_algorithms():
    """Verify that both algorithms produce the same MST weight for a sample graph."""
    print("Verifying algorithms...")

    # Create a test graph
    test_graph = Graph(5)
    test_graph.add_edge(0, 1, 2)
    test_graph.add_edge(0, 3, 6)
    test_graph.add_edge(1, 2, 3)
    test_graph.add_edge(1, 3, 8)
    test_graph.add_edge(1, 4, 5)
    test_graph.add_edge(2, 4, 7)
    test_graph.add_edge(3, 4, 9)

    # Run Prim's algorithm
    prim_mst, prim_weight, _, _ = prim(test_graph)

    # Run Kruskal's algorithm
    kruskal_mst, kruskal_weight, _, _ = kruskal(test_graph)

    # Verify results
    print(f"Prim's MST: {prim_mst}, Total Weight: {prim_weight}")
    print(f"Kruskal's MST: {kruskal_mst}, Total Weight: {kruskal_weight}")

    if prim_weight == kruskal_weight:
        print("✓ Algorithms produce the same MST weight\n")
        return True
    else:
        print("✗ Algorithms produce different MST weights\n")
        return False


def main():
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Verify that algorithms produce correct results
    if not verify_algorithms():
        print("Algorithm verification failed. Please check implementations.")
        return

    # Define graph sizes for benchmarking
    graph_sizes = [10, 50, 100, 200, 500, 800]

    # Run benchmarks
    print("Running benchmarks...")
    benchmark = Benchmark(graph_sizes)
    benchmark.run_all_benchmarks(prim, kruskal)

    # Get results
    results, _ = benchmark.get_results()

    # Create and display tables
    sparse_table, dense_table = Visualizer.create_results_table(graph_sizes, results)

    print("\nSparse Graph Results:")
    print(sparse_table.to_string(index=False))

    print("\nDense Graph Results:")
    print(dense_table.to_string(index=False))

    # Save tables to CSV
    sparse_table.to_csv("output/sparse_results.csv", index=False)
    dense_table.to_csv("output/dense_results.csv", index=False)

    # Create and save visualizations
    print("\nGenerating visualizations...")
    Visualizer.plot_execution_times(graph_sizes, results, save_path="output/execution_time.png")
    Visualizer.plot_memory_usage(graph_sizes, results, save_path="output/memory_usage.png")

    print("Visualizations saved to:")
    print("- output/execution_time.png")
    print("- output/memory_usage.png")

    print("\nBenchmark complete!")
    print("Results saved to the 'output' directory.")


if __name__ == "__main__":
    main()