import networkx as nx

import graphs
import algorithms
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

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


def calculate_page_rank(graph, graph_name):
    distributions, stationary_distribution = algorithms.page_rank(graph, graph_name)

    figure, axis = plt.subplots(1, 2)

    axis[0].plot(distributions[0])

    axis[0].set_title('uniform')

    axis[1].plot(stationary_distribution)
    axis[1].set_title('stationary')

    if len(distributions) > 1:
        axis[1].plot(distributions[1])
        axis[1].set_title('clique')

    plt.show()


def calculate_eigenvalues_ratio(all_graphs):
    for graph_name, graph in all_graphs.items():
        eigen_values = algorithms.power_iteration(graph)
        print('graph:{}, eigenValues:{}, ratio:{}'.format(graph_name, eigen_values, eigen_values[1]/eigen_values[0]))


if __name__ == '__main__':
    n = 2**14
    all_graphs = graphs.get_graphs(n)

    #a = all_graphs['toffee']

    #for i in range(10):
    #    q, r = np.linalg.qr(a)
    #    a = np.dot(r, q)

    #np.set_printoptions(precision=3)
    #np.set_printoptions(suppress=True)
    #print(a)

    #lolipop_graph_x = nx.from_numpy_array(all_graphs['toffee'])
    #pr = nx.pagerank(lolipop_graph_x, 1, max_iter=1000)
    #plt.plot(pr.values())
    #plt.show()



    #calculate_cover_times(all_graphs, n)
    #calculate_eigenvalues_ratio(all_graphs)
    calculate_page_rank(all_graphs['clique'], 'clique')




