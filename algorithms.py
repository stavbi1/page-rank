import numpy as np

import graphs


def is_covered(graph_size, covered):
    return len(covered) == graph_size


def get_cover_time(graph, start_vector):
    cover_time = 1
    graph_size = graph.shape[0]

    possible_vertices = np.where(start_vector)[0]
    current_vertex = np.random.choice(possible_vertices)

    covered = {current_vertex}

    while not is_covered(graph_size, covered):
        possible_vertices = np.where(graph[:, current_vertex])[0]
        current_vertex = np.random.choice(possible_vertices)

        covered.add(current_vertex)
        cover_time += 1

    return cover_time


def proj_w_on_u(w, u):
    return (np.dot(w, u) / (np.linalg.norm(u)**2)) * u


def power_iteration(graph):
    graph_size = graph.shape[0]
    eigen_vectors = np.empty((graph_size, 2))
    eigen_values = np.array([])

    for eigen_vector_index in range(2):
        Wprev = np.random.choice([0, 1], size=(graph_size,))

        if eigen_vector_index == 0:
            Uprev = Wprev
        else:
            Uprev = Wprev - proj_w_on_u(Wprev, eigen_vectors[:, 0])

        for iteration_number in range(100):
            Vcurr = np.dot(graph, Uprev)

            if eigen_vector_index != 0:
                Vcurr = Vcurr - proj_w_on_u(Vcurr, eigen_vectors[:, 0])

            Vcurr_norm = np.linalg.norm(Vcurr)

            if Vcurr_norm != 0:
                Ucurr = Vcurr / Vcurr_norm
            else:
                Ucurr = Vcurr

            diff = np.linalg.norm(Ucurr - Uprev)
            Uprev = Ucurr

            if diff < 2**-8:
                print(
                    'diff:{}, iteration:{}, eigenvalue:{}\n'.format(
                        diff,
                        iteration_number,
                        np.linalg.norm(np.dot(graph, Ucurr))
                    )
                )
                break

        eigen_vectors[:, eigen_vector_index] = Ucurr
        eigen_values = np.append(eigen_values, np.linalg.norm(np.dot(graph, Ucurr)))

    return eigen_values


def get_starting_distributions(n, graph_name):
    distributions = [np.ones(n)]
    #distributions = [np.append(np.zeros(n-1), 1)]

    #if graph_name == 'lolipop' or graph_name == 'toffee':
        #distributions.append(np.append(np.zeros(n-1), 1))

    return distributions


def page_rank(graph, graph_name, N=2**8):
    n = graph.shape[0]
    t = 4000

    distribution_vectors = []
    starting_distributions = get_starting_distributions(n, graph_name)
    stationary_distribution = graphs.get_stationary_distribution(graph)

    for starting_distribution_idx, starting_distribution in enumerate(starting_distributions):
        distribution_vector = np.zeros(n)

        for t_iteration in range(t):
            possible_vertices = np.where(starting_distribution)[0]
            current_vertex = np.random.choice(possible_vertices)
            distribution_vector[current_vertex] += 1

            for step in range(N):
                possible_vertices = np.where(graph[:, current_vertex])[0]
                current_vertex = np.random.choice(possible_vertices)
                distribution_vector[current_vertex] += 1

            diff = np.linalg.norm(stationary_distribution - (distribution_vector / ((N + 1) * (t_iteration + 1))))
            if diff < 2**-6:
                print('iteration:{}'.format(t_iteration))
                break

        distribution_vector /= (N + 1) * (t_iteration + 1)

        distribution_vectors.append(distribution_vector)

    return distribution_vectors, stationary_distribution
