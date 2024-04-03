import time
import matplotlib.pyplot as plt
from Algorithms import BFS, DFS
from generate_graphs import average_graph, horizontal_graph, vertical_graph
import os

def measure_time(algorithm, graph, n):
    start_time = time.time()
    algorithm(graph, n)
    end_time = time.time()

    return end_time - start_time


def measure_sort(algorithm):
    n_values = []
    time_values_horizontal = []
    time_values_vertical = []
    time_values_average = []

    test_vals = range(100, 1000, 10)
    
    print(f"{algorithm.__name__} Performance:")
    for test_num in test_vals:
        # Measure time for medium graph
        avg_graph = average_graph(test_num)
        start_node = next(iter(avg_graph))
        exec_time_med = measure_time(algorithm, avg_graph, start_node)
        print("For graph with vertexes", test_num, "time execution: ", exec_time_med)
        time_values_average.append(exec_time_med)

    test_vals = range(100, 1000, 10)
    
    for test_num in test_vals:
        n_values.append(test_num)
        # Measure time for vertical graph
        vert_graph = vertical_graph(test_num)
        start_node = next(iter(vert_graph))
        exec_time_vertical = measure_time(algorithm, vert_graph, start_node)
        time_values_vertical.append(exec_time_vertical)

        # Measure time for horizontal graph
        hor_graph = horizontal_graph(test_num)
        start_node = next(iter(hor_graph))
        exec_time_horizontal = measure_time(algorithm, hor_graph, start_node)
        time_values_horizontal.append(exec_time_horizontal)

    plt.plot(n_values, time_values_horizontal, label='Horizontal Graph')
    plt.plot(n_values, time_values_vertical, label='Vertical Graph')
    plt.plot(n_values, time_values_average, label='Average Graph')

    plt.xlabel("Array length")
    plt.ylabel("Time (s)")
    plt.title(f"{algorithm.__name__} Performance for Different Graphs")
    plt.legend()
    path = os.path.join(os.getcwd(),'Graphs',f'{algorithm.__name__}_performance.png')
    plt.savefig(path)
    plt.close()

algorithms = [BFS, DFS]
for algorithm in algorithms:
    measure_sort(algorithm)
    
