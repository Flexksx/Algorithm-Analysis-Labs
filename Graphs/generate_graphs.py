import random
import string
import math


def generate_vertex(vertices):
        while True:
            vertex = ''.join(random.choices(string.ascii_lowercase, k=5))
            if vertex not in vertices:
                return vertex

def vertical_graph(n):
    graph = {}
    vertices = []
    second_row = []
    start_node = generate_vertex(vertices)
    vertices.append(start_node)

    for i in range(4):
        neighbor = generate_vertex(vertices)
        vertices.append(neighbor)
        second_row.append(neighbor)

    graph[start_node] = second_row
    for node in second_row:
        for j in range(int((n-5)/4)):
            l = []
            secondary_neighbor = generate_vertex(vertices)
            vertices.append(secondary_neighbor)
            l.append(secondary_neighbor)
            graph[node] = l
            node = secondary_neighbor
        graph[node] = []
    return graph


def horizontal_graph(n):
    graph = {}
    vertexes = []
    second_row = []
    def generate_vertex(vertexes):
        while True:
            vertex = ''.join(random.choices(string.ascii_lowercase, k=5))
            if vertex not in vertexes:
                return vertex

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

def average_graph(n):
    graph = {}
    vertexes = []
    second_row = []
    x = int(math.sqrt(n))
    def generate_vertex(vertexes):
        while True:
            vertex = ''.join(random.choices(string.ascii_lowercase, k=5))
            if vertex not in vertexes:
                return vertex

    start_node = generate_vertex(vertexes)
    vertexes.append(start_node)

    for i in range(x):
        neighbor = generate_vertex(vertexes)
        vertexes.append(neighbor)
        second_row.append(neighbor)

    graph[start_node] = second_row

    for node in second_row:
        l = []
        for j in range(x):
            secondary_neighbor = generate_vertex(vertexes)
            vertexes.append(secondary_neighbor)
            l.append(secondary_neighbor)
        graph[node] = l
        for nod in l:
            graph[nod] = []

    return graph