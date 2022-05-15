import matplotlib.pyplot as plt

from search import Search, A_STAR, UNIFORM_COST, MANHATTAN_DISTANCE, MISPLACED_TILE
from test_search import TestSearch


def get_data(algorithm, heuristic):
    """
    Collect the data for one algorithm.

    :param algorithm: Algorithm to be used.
    :param heuristic: Heuristic to be used.
    :return: Depth, Maximum Queue Size, No. of nodes expanded, Time taken for the alorithm.
    """
    d_list = []
    q_list = []
    c_list = []
    t_list = []

    for test_case in TestSearch.TESTS:
        (test_board, test_depth) = test_case
        s = Search(algorithm, heuristic, test_board)
        s.search()
        d, q, c, t = s.get_statistics()
        d_list.append(d)
        q_list.append(q)
        c_list.append(c)
        t_list.append(t)

    return d_list, q_list, c_list, t_list


def plot_data():
    """
    Function to plot data for sample test cases.

    :return:
    """
    # Collect data for the algorithms
    d_uc, q_uc, c_uc, t_uc = get_data(UNIFORM_COST, 0)
    d_a_mt, q_a_mt, c_a_mt, t_a_mt = get_data(A_STAR, MISPLACED_TILE)
    d_a_md, q_a_md, c_a_md, t_a_md = get_data(A_STAR, MANHATTAN_DISTANCE)

    # Plot depth vs. max queue size
    plt.figure("Figure 1")
    p1 = plt.plot(d_uc, q_uc)
    p2 = plt.plot(d_a_mt, q_a_mt)
    p3 = plt.plot(d_a_md, q_a_md)
    plt.xlabel("Depth")
    plt.ylabel("Max Queue Size")
    plt.title("Depth vs. Max Queue Size")
    plt.legend((p1[0], p2[0], p3[0]), ("Uniform Cost", "A* Misplaced Tile", "A* Manhattan Distance"))
    plt.show()

    # Plot depth versus expanded nodes
    plt.figure("Figure 2")
    p1 = plt.plot(d_uc, c_uc)
    p2 = plt.plot(d_a_mt, c_a_mt)
    p3 = plt.plot(d_a_md, c_a_md)
    plt.xlabel("Depth")
    plt.ylabel("Expanded Nodes")
    plt.title("Depth vs. Expanded Nodes")
    plt.legend((p1[0], p2[0], p3[0]), ("Uniform Cost", "A* Misplaced Tile", "A* Manhattan Distance"))
    plt.show()

    # Plot depth versus expanded nodes
    plt.figure("Figure 3")
    p1 = plt.plot(d_uc, t_uc)
    p2 = plt.plot(d_a_mt, t_a_mt)
    p3 = plt.plot(d_a_md, t_a_md)
    plt.xlabel("Depth")
    plt.ylabel("Time")
    plt.title("Depth vs. Time")
    plt.legend((p1[0], p2[0], p3[0]), ("Uniform Cost", "A* Misplaced Tile", "A* Manhattan Distance"))
    plt.show()


if __name__ == "__main__":
    plot_data()
