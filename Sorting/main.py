from quick import quick_sort
from shell import shell_sort
from heap import heap_sort
from merge import merge_sort
from random import randint, random
from time import time
import matplotlib.pyplot as plt
import json

# Define sorting algorithms
sorting_algorithms = {
    "quick_sort": quick_sort,
    "shell_sort": shell_sort,
    "heap_sort": heap_sort,
    "merge_sort": merge_sort,
}

# Define array sizes for testing
array_sizes=list(range(10,50000,1000))
# Define types of tests
test_types = ["int", "long_int", "float"]

# Initialize results dictionary
results = {algorithm: {test_type: {size: [] for size in array_sizes} for test_type in test_types}
           for algorithm in sorting_algorithms}

# Perform tests
for algorithm_name, algorithm in sorting_algorithms.items():
    for test_type in test_types:
        for size in array_sizes:
            # Generate test array based on test type and size
            if test_type == "int":
                test_arr = [randint(0, 100) for _ in range(size)]
            elif test_type == "long_int":
                test_arr = [randint(1000, 5000) for _ in range(size)]
            else:
                test_arr = [random() * randint(0, 100) for _ in range(size)]

            # Measure execution time
            start_time = time()
            algorithm(test_arr)
            end_time = time()

            # Record results
            results[algorithm_name][test_type][size].append(
                end_time - start_time)



for algorithm in results:
    for test_type in results[algorithm]:
        x_axis = list(results[algorithm][test_type].keys())
        y_axis = [sum(results[algorithm][test_type][size]) / len(results[algorithm][test_type][size]) for size in x_axis]
        plt.plot(x_axis, y_axis, label=f"{algorithm} ({test_type})")
    plt.title(f"Sorting Algorithms Performance")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.legend(['quick_sort (int)', 'quick_sort (long_int)', 'quick_sort (float)', 'shell_sort (int)', 'shell_sort (long_int)', 'shell_sort (float)', 'heap_sort (int)', 'heap_sort (long_int)', 'heap_sort (float)', 'merge_sort (int)', 'merge_sort (long_int)', 'merge_sort (float)'])
plt.savefig(f"{algorithm}.png")
plt.close()