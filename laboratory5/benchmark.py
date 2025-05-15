import time
import statistics
from graph import Graph


class Benchmark:
    def __init__(self, graph_sizes, num_trials=5):
        """
        Initialize benchmark parameters.

        Args:
            graph_sizes: List of vertex counts for testing
            num_trials: Number of trials to run for each configuration
        """
        self.graph_sizes = graph_sizes
        self.num_trials = num_trials
        self.results = {
            'sparse': {
                'prim': {'time': [], 'memory': []},
                'kruskal': {'time': [], 'memory': []}
            },
            'dense': {
                'prim': {'time': [], 'memory': []},
                'kruskal': {'time': [], 'memory': []}
            }
        }

    def run_benchmark(self, algorithm_func, graph_type, size):
        """
        Run a single benchmark for a given algorithm and graph type.

        Args:
            algorithm_func: Function implementing the algorithm
            graph_type: 'sparse' or 'dense'
            size: Number of vertices in the graph

        Returns:
            Tuple of (avg_time, avg_memory)
        """
        times = []
        memories = []

        for _ in range(self.num_trials):
            # Generate graph based on type
            if graph_type == 'sparse':
                graph = Graph.generate_sparse_graph(size)
            else:  # dense
                graph = Graph.generate_dense_graph(size)

            # Run algorithm
            _, _, execution_time, memory_used = algorithm_func(graph)

            times.append(execution_time)
            memories.append(memory_used)

        # Calculate averages
        avg_time = statistics.mean(times)
        avg_memory = statistics.mean(memories)

        return avg_time, avg_memory

    def run_all_benchmarks(self, prim_func, kruskal_func):
        """
        Run all benchmarks for both algorithms on sparse and dense graphs.

        Args:
            prim_func: Function implementing Prim's algorithm
            kruskal_func: Function implementing Kruskal's algorithm
        """
        for size in self.graph_sizes:
            print(f"Benchmarking graphs with {size} vertices...")

            # Sparse graph benchmarks
            prim_time, prim_memory = self.run_benchmark(prim_func, 'sparse', size)
            kruskal_time, kruskal_memory = self.run_benchmark(kruskal_func, 'sparse', size)

            self.results['sparse']['prim']['time'].append(prim_time)
            self.results['sparse']['prim']['memory'].append(prim_memory)
            self.results['sparse']['kruskal']['time'].append(kruskal_time)
            self.results['sparse']['kruskal']['memory'].append(kruskal_memory)

            # Dense graph benchmarks
            prim_time, prim_memory = self.run_benchmark(prim_func, 'dense', size)
            kruskal_time, kruskal_memory = self.run_benchmark(kruskal_func, 'dense', size)

            self.results['dense']['prim']['time'].append(prim_time)
            self.results['dense']['prim']['memory'].append(prim_memory)
            self.results['dense']['kruskal']['time'].append(kruskal_time)
            self.results['dense']['kruskal']['memory'].append(kruskal_memory)

            print(f"  Completed size {size}")

        print("All benchmarks completed.")

    def get_results(self):
        """Return the benchmark results."""
        return self.results, self.graph_sizes