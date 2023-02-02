import numpy as np


def to_stochastic(graph):
    return graph / graph.sum(axis=0)[None, :]


def get_clique(n):
    adj_matrix = np.ones(shape=(n, n)) / n

    return adj_matrix


def get_ring(n):
    adj_matrix = np.logical_or(np.eye(n, k=-1), np.logical_or(np.eye(n, k=1), np.eye(n, k=0))).astype(int)
    adj_matrix[0, n - 1] = 1
    adj_matrix[n - 1, 0] = 1

    return to_stochastic(adj_matrix)


def get_lolipop(n):
    adj_matrix = np.logical_or(np.eye(n, k=-1), np.logical_or(np.eye(n, k=1), np.eye(n, k=0))).astype(int)

    adj_matrix[int(n/2) - 1:, int(n/2) - 1:] = 1

    return to_stochastic(adj_matrix)


def get_toffee(n):
    left_upper_quarter_mask = np.zeros(shape=(n, n))
    left_upper_quarter_mask[:int(n/2), :int(n/2)] = 1

    adj_matrix = np.logical_and(
        np.logical_or(
            np.eye(n, k=-1),
            np.logical_or(
                np.eye(n, k=1),
                np.eye(n, k=0)
            )
        ),
        left_upper_quarter_mask
    ).astype(int)

    adj_matrix[0, int(n/2)] = 1
    adj_matrix[int(n/2), 0] = 1

    adj_matrix[int(n / 2) - 1, int(3*n/4)] = 1
    adj_matrix[int(3*n/4), int(n / 2) - 1] = 1

    adj_matrix[int(n/2):int(3*n/4), int(n/2):int(3*n/4)] = 1

    adj_matrix[int(3*n/4):, int(3*n/4):] = 1

    return to_stochastic(adj_matrix)


def get_graphs(n):
    return {
        #'clique': get_clique(n),
        #'ring': get_ring(n),
        #'lolipop': get_lolipop(n),
        'toffee': get_toffee(n)
    }