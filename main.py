import graphs
import algorithms
import numpy as np


def print_cover_times(graph_name, cover_times, is_uniform):
    mean_time = np.mean(cover_times)
    max_time = np.max(cover_times)
    min_time = np.min(cover_times)

    print(
        'graph:{}\nmean={}, max={}, min={}\nis uniform={}\n\n'.format(
            graph_name,
            mean_time,
            max_time,
            min_time,
            is_uniform
        )
    )


def calculate_cover_times(all_graphs, n):
    repeat = 10
    uniform_vector = np.ones(n)
    last_vertex_vector = np.append(np.zeros(n-1), 1)

    for graph_name, graph in all_graphs.items():
        cover_times = np.array([])

        for probability_vector_idx, probability_vector in enumerate([uniform_vector, last_vertex_vector]):
            for i in range(repeat):
                cover_times = np.append(cover_times, algorithms.get_cover_time(graph, probability_vector))
                print('done {} of {}'.format(i, graph_name))

            print_cover_times(graph_name, cover_times, probability_vector_idx == 0)


if __name__ == '__main__':
    n = 6
    all_graphs = graphs.get_graphs(n)

    #calculate_cover_times(all_graphs, n)
    print(algorithms.power_iteration(all_graphs['ring']))
