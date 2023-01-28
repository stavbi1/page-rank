import numpy as np


def is_covered(graph_size, covered):
    return len(covered) == graph_size


def get_cover_time(graph, start_vector):
    cover_time = 1
    graph_size = graph.shape[0]

    possible_vertices = np.where(start_vector)[0]
    current_vertex = np.random.choice(possible_vertices)

    covered = {current_vertex}

    while not is_covered(graph_size, covered):
        possible_vertices = np.where(graph[current_vertex])[0]
        current_vertex = np.random.choice(possible_vertices)

        covered.add(current_vertex)
        cover_time += 1

    return cover_time


def power_iteration(graph):
    graph_size = graph.shape[0]
    Uprev = np.random.choice([0, 1], size=(graph_size,))

    for i in range(100):
        Vcurr = np.matmul(graph, Uprev)
        Ucurr = Vcurr / np.linalg.norm(Vcurr)

        diff = np.linalg.norm(Ucurr - Uprev)
        Uprev = Ucurr

        if diff < 2**-6:
            print('diff:{}, iteration:{}'.format(diff, i))
            return Ucurr

    return Ucurr
