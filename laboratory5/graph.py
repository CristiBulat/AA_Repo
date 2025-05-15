import random
import networkx as nx


class Graph:
    def __init__(self, num_vertices):
        """Initialize a graph with given number of vertices."""
        self.num_vertices = num_vertices
        self.adjacency_list = [{} for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        """Add an undirected edge between vertices u and v with given weight."""
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError("Vertex index out of range")

        # Add edge in both directions (undirected graph)
        self.adjacency_list[u][v] = weight
        self.adjacency_list[v][u] = weight

    def get_adjacency_list(self):
        """Return the adjacency list representation of the graph."""
        return self.adjacency_list

    def get_edges(self):
        """Return all edges in the graph as (u, v, weight) tuples."""
        edges = []
        for u in range(self.num_vertices):
            for v, weight in self.adjacency_list[u].items():
                if u < v:  # To avoid duplicates in undirected graph
                    edges.append((u, v, weight))
        return edges

    @staticmethod
    def generate_sparse_graph(num_vertices, edge_probability=0.2, min_weight=1, max_weight=100):
        """
        Generate a sparse graph with given number of vertices.
        Each potential edge is added with probability edge_probability.
        """
        graph = Graph(num_vertices)

        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):  # Only consider upper triangle
                if random.random() < edge_probability:
                    weight = random.randint(min_weight, max_weight)
                    graph.add_edge(u, v, weight)

        # Ensure the graph is connected
        Graph._ensure_connected(graph)

        return graph

    @staticmethod
    def generate_dense_graph(num_vertices, edge_probability=0.8, min_weight=1, max_weight=100):
        """
        Generate a dense graph with given number of vertices.
        Each potential edge is added with probability edge_probability.
        """
        graph = Graph(num_vertices)

        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):  # Only consider upper triangle
                if random.random() < edge_probability:
                    weight = random.randint(min_weight, max_weight)
                    graph.add_edge(u, v, weight)

        # Ensure the graph is connected
        Graph._ensure_connected(graph)

        return graph

    @staticmethod
    def _ensure_connected(graph):
        """Ensure the graph is connected by adding edges if necessary."""
        # Build a NetworkX graph for connected component analysis
        G = nx.Graph()
        G.add_nodes_from(range(graph.num_vertices))

        for u in range(graph.num_vertices):
            for v, weight in graph.adjacency_list[u].items():
                if u < v:  # Add each edge only once
                    G.add_edge(u, v, weight=weight)

        # Find connected components
        components = list(nx.connected_components(G))

        # If more than one component, add edges to connect them
        while len(components) > 1:
            # Select two random nodes from different components
            comp1 = random.choice(list(components[0]))
            comp2 = random.choice(list(components[1]))

            # Connect with a random weight
            weight = random.randint(1, 100)
            graph.add_edge(comp1, comp2, weight)

            # Update the graph in NetworkX
            G.add_edge(comp1, comp2, weight=weight)

            # Recalculate connected components
            components = list(nx.connected_components(G))