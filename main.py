import graphs
import algorithms
import numpy as np
import matplotlib.pyplot as plt

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

    for graph_name, graph in all_graphs.items():
        cover_times = np.array([])

        starting_distributions = algorithms.get_starting_distributions(n, graph_name)
        for probability_vector_idx, probability_vector in enumerate(starting_distributions):
            for i in range(repeat):
                cover_times = np.append(cover_times, algorithms.get_cover_time(graph, probability_vector))
                print('done {} of {}'.format(i, graph_name))

            print_cover_times(graph_name, cover_times, probability_vector_idx == 0)


def calculate_page_rank(all_graphs):
    distribution, histograms = algorithms.page_rank(all_graphs['lolipop'], 'lolipop')
    print(distribution)

    figure, axis = plt.subplots(1, 2)

    axis[0].plot(distribution[0])
    axis[0].set_title('uniform')

    axis[1].plot(distribution[1])
    axis[1].set_title('clique')

    plt.show()


def calculate_eigenvalues_ratio(all_graphs):
    for graph_name, graph in all_graphs.items():
        eigen_values = algorithms.power_iteration(graph)
        print('graph:{}, eigenValues:{}, ratio:{}'.format(graph_name, eigen_values, eigen_values[0]/eigen_values[1]))




if __name__ == '__main__':
    n = 2**9
    all_graphs = graphs.get_graphs(n)

    calculate_cover_times(all_graphs, n)
    #calculate_eigenvalues_ratio(all_graphs)



