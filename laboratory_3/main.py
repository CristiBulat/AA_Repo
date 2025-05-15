import os
from algorithms import dfs, bfs
from graph_generators import GraphGenerator
from performance import measure_performance
from visualization import plot_results


def ensure_results_dir():
    """Create results directory if it doesn't exist."""
    if not os.path.exists('results'):
        os.makedirs('results')


def run_analysis():
    """Run the complete analysis for all graph types and sizes."""
    ensure_results_dir()

    graph_generator = GraphGenerator()

    # Define graph types and corresponding generation methods
    graph_types = {
        'finite': graph_generator.generate_finite_graph,
        'complete': graph_generator.generate_complete_graph,
        'tree': graph_generator.generate_tree_graph,
        'sparse': graph_generator.generate_sparse_graph,
        'dense': graph_generator.generate_dense_graph,
        'bipartite': graph_generator.generate_bipartite_graph,
        'cyclic': graph_generator.generate_cyclic_graph,
        'acyclic': graph_generator.generate_acyclic_graph,
        'multigraph': graph_generator.generate_multigraph,
        'pseudograph': graph_generator.generate_pseudograph,
        'regular': graph_generator.generate_regular_graph,
        'weighted': graph_generator.generate_weighted_graph,
        'directed': graph_generator.generate_directed_graph
    }

    sizes = [10, 50, 100, 200, 500, 800]
    results = {}

    for graph_type, generator in graph_types.items():
        print(f"Analyzing {graph_type} graphs...")

        dfs_metrics = []
        bfs_metrics = []

        for size in sizes:
            print(f"  Size: {size}")
            graph = generator(size)

            print("    Running DFS...")
            dfs_result = measure_performance(dfs, graph)
            dfs_metrics.append(dfs_result)

            print("    Running BFS...")
            bfs_result = measure_performance(bfs, graph)
            bfs_metrics.append(bfs_result)

        # Store results
        results[graph_type] = {
            'sizes': sizes,
            'dfs': dfs_metrics,
            'bfs': bfs_metrics
        }

        # Create visualization
        plot_results(sizes, dfs_metrics, bfs_metrics, graph_type)

        # Generate table data for report
        print(f"\nResults for {graph_type} graphs:")
        print("Graph Size | DFS Time (s) | BFS Time (s) | DFS Memory | BFS Memory")
        print("-" * 70)

        for i, size in enumerate(sizes):
            print(f"{size:10} | {dfs_metrics[i]['time']:.6f} | {bfs_metrics[i]['time']:.6f} | "
                  f"{int(dfs_metrics[i]['memory']):10} | {int(bfs_metrics[i]['memory']):10}")

        print("\n")

    return results


if __name__ == "__main__":
    results = run_analysis()
    print("Analysis complete. Results saved to 'results' directory.")