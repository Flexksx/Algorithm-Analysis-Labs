import time
import matplotlib.pyplot as plt
from Algorithms import BFS, DFS
from generate_graphs import *
import os
import networkx as nx

def measure_time(algorithm, graph, n):
    start_time = time.time()
    algorithm(graph, n)
    end_time = time.time()

    return end_time - start_time


def measure_performance(algorithm):
    n_values = []
    time_sparse = []
    time_dense = []
    time_average = []
    time_shallow = []
    test_node_values = range(100, 2000, 10)
    print(f"Measuring performance for {algorithm.__name__}")
    for test_num in test_node_values:
        print(f"Measuring performance for {test_num} nodes")
        n_values.append(test_num)
        # Measure time for medium graph
        avg_graph = generate_graph(test_num,p=0.05)
        start_node = next(iter(avg_graph))
        exec_time_med = measure_time(algorithm, avg_graph, start_node)
        time_average.append(exec_time_med)

        # Measure time for vertical graph
        sparse_graph = generate_graph(test_num,p=0.01)
        start_node = next(iter(sparse_graph))
        exec_time_vertical = measure_time(algorithm, sparse_graph, start_node)
        time_dense.append(exec_time_vertical)

        # Measure time for horizontal graph
        dense_graph = generate_graph(test_num,p=0.1)
        start_node = next(iter(dense_graph))
        exec_time_horizontal = measure_time(algorithm, dense_graph, start_node)
        time_sparse.append(exec_time_horizontal)

        # Measure time for shallow graph
        shall_graph = shallow_graph(test_num)
        start_node = next(iter(shall_graph))
        exec_time_shallow = measure_time(algorithm, shall_graph, start_node)
        time_shallow.append(exec_time_shallow)
        

    plt.plot(n_values, time_sparse, label='Sparse Graph')
    plt.plot(n_values, time_dense, label='Dense Graph')
    plt.plot(n_values, time_average, label='Average Graph')
    plt.plot(n_values, time_shallow, label='Shallow Graph')

    plt.xlabel("Node count")
    plt.ylabel("Time (s)")
    plt.title(f"{algorithm.__name__} Performance for Different Graphs")
    plt.legend()
    path = os.path.join(os.getcwd(),'Graphs',f'{algorithm.__name__}_performance.png')
    plt.savefig(path)
    plt.close()

def draw_graph(graph):
    G = nx.Graph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)
    pos = nx.spring_layout(G, k=0.15, iterations=20)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=15)
    plt.show()

algorithms = [BFS, DFS]
for algorithm in algorithms:
    measure_performance(algorithm)

# graph = shallow_graph(50)

# draw_graph(graph)