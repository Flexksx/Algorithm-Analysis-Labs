import random
import string
import math


def generate_vertex(vertices):
        while True:
            vertex = ''.join(random.choices(string.ascii_lowercase, k=5))
            if vertex not in vertices:
                return vertex


def generate_graph(n, p=0.1):
    

    graph = {}
    vertices = []

    for _ in range(n):
        vertex = generate_vertex(vertices)
        vertices.append(vertex)
        graph[vertex] = []

    for vertex in graph:
        for other_vertex in graph:
            if vertex != other_vertex and random.random() < p:
                graph[vertex].append(other_vertex)

    return graph


def shallow_graph(n):
    """
    Generates a shallow graph with 'n' nodes.

    Args:
        n (int): The number of nodes in the graph.

    Returns:
        dict: A dictionary representing the generated graph, where the keys are the nodes and the values are lists of neighboring nodes.
    """
    graph = {}
    vertexes = []
    second_row = []
    start_node = generate_vertex(vertexes)
    vertexes.append(start_node)

    for i in range(4):
        neighbor = generate_vertex(vertexes)
        vertexes.append(neighbor)
        second_row.append(neighbor)

    graph[start_node] = second_row

    for node in second_row:
        l = []
        for j in range(int((n-5)/4)):
            secondary_neighbor = generate_vertex(vertexes)
            vertexes.append(secondary_neighbor)
            l.append(secondary_neighbor)
        graph[node] = l
        for nod in l:
            graph[nod] = []

    return graph