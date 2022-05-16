import time

from heapq import *

from board import Board

# Algorithms
UNIFORM_COST = 0
A_STAR = 1

# Heuristics
MISPLACED_TILE = 0
MANHATTAN_DISTANCE = 1


class Search(object):
    """
    Class for finding a solution to a provided 8-Puzzle using search.
    """
    def __init__(self, algorithm, heuristic, initial_state):
        if algorithm != A_STAR and algorithm != UNIFORM_COST:
            exit(-1)
        if algorithm == A_STAR and \
                (heuristic != MANHATTAN_DISTANCE and heuristic != MISPLACED_TILE):
            exit(-1)
        self.algorithm = algorithm
        self.heuristic = heuristic
        self.initial_state = initial_state
        self.max_queue_size = 0
        self.depth = 0
        self.count_nodes_expanded = 0
        self.start_time = 0
        self.end_time = 0
        self.visited = dict()

    def make_queue(self, node):
        """
        Make a queue that can hold nodes.

        :param node: The first node to add to the queue
        :return: The queue
        """
        nodes = []
        heappush(nodes, node)
        return nodes

    def make_node(self, state):
        """
        Make a single node.

        :param state: The state for which a node is to be created.
        :return: The created node.
        """
        cost, board_state, parent = state
        b = Board(board_state, parent)
        b.cost = cost
        if self.algorithm == A_STAR:
            if self.heuristic == MANHATTAN_DISTANCE:
                b.cost = b.cost + b.manhattan_distance()
            elif self.heuristic == MISPLACED_TILE:
                b.cost = b.cost + b.misplaced_tile()
        return b

    def empty(self, nodes):
        """
        Check if the list of nodes is empty.

        :param nodes: The list of nodes.
        :return: Whether the list is empty or not.
        """
        return len(nodes) == 0

    def remove_front(self, nodes):
        """
        Remove the node with the cheapest cost.

        :param nodes: The list of nodes from which the cheapest node needs to be popped.
        :return: The cheapest node.
        """
        node = heappop(nodes)
        if self.algorithm == A_STAR:
            print("The best state to expand with a g(n) = {} and h(n) = {} is...".format(node.depth,
                                                                                         node.cost - node.depth))
        elif self.algorithm == UNIFORM_COST:
            print("The best state to expand with a g(n) = {} is...".format(node.depth))
        node.print_board()
        return node

    def queuing_function(self, nodes, children):
        """
        Function for queueing child nodes of a parent.

        :param nodes: The list into which the child nodes need to be inserted.
        :param children: The list of children to be inserted.
        :return: The updated list of nodes.
        """

        for child in children:

            # If the algorithm is uniform cost, then just add 1 because
            # just one move is required from one state to the next. Otherwise, the
            # heuristic cost also needs to be considered.
            if self.algorithm == UNIFORM_COST:
                child.cost = 1 + child.parent.cost
            elif self.algorithm == A_STAR:
                # Parameters for calculating cost of the child node
                # g_x is the current depth of the child node. h_x is the
                # heuristic cost of the node.
                g_x = 1 + child.depth
                h_x = 0
                if self.heuristic == MANHATTAN_DISTANCE:
                    h_x = child.manhattan_distance()
                elif self.heuristic == MISPLACED_TILE:
                    h_x = child.misplaced_tile()
                child.cost = g_x + h_x

            # Push the child into the heap
            heappush(nodes, child)

        # Keep a track of the queue size.
        if len(nodes) > self.max_queue_size:
            self.max_queue_size = len(nodes)

        return nodes

    def expand(self, node, operators):
        """
        Expand a node to its children.

        :param node: The node for which the children need to be expanded.
        :param operators:
        :return: A list of nodes.
        """
        self.count_nodes_expanded = self.count_nodes_expanded + 1
        self.visited[node] = 1
        return node.generate_children(self.visited)

    def general_search(self, queuing_function):
        """
        A general search function based on the pseudocode provided by the project 1 handout.

        :param queuing_function: Function for queuing the nodes.
        :return: The goal state or None if no solution found.
        """
        problem_initial_state = 0, self.initial_state, None

        # Insert the first node into the queue
        nodes = self.make_queue(self.make_node(problem_initial_state))

        while True:
            # Check if there are no more states to expand.
            # If None, then there's no solution to the problem's
            # initial state.
            if self.empty(nodes):
                return None

            # Remove the cheapest node from the list of nodes
            node = self.remove_front(nodes)

            # Get the cost & the board from the node
            if node.goal_test(node.state):
                return node

            # Use the provided queueing function, otherwise own function.
            if queuing_function is not None:
                nodes = queuing_function(nodes, self.expand(node, None))
            else:
                nodes = self.queuing_function(nodes, self.expand(node, None))

    def print_search_stats(self, node):
        """
        Print the statistics of the search performed.

        :return: Nothing.
        """
        if node is None:
            print("8-Puzzle provided is not solvable.")
            print("Number of nodes expanded: {0}".format(self.count_nodes_expanded))
            print("Max queue size: {0}".format(self.max_queue_size))
            print("Time taken: {0:.2f}".format(self.end_time - self.start_time))
            return

        self.depth = node.depth
        print("Solution depth was: {0}".format(self.depth))
        print("Number of nodes expanded: {0}".format(len(self.visited)))
        print("Max queue size: {0}".format(self.max_queue_size))
        print("Time taken: {0:.2f} seconds".format(self.end_time - self.start_time))

    def get_statistics(self):
        """
        Return a tuple of all the search statistics.

        :return: Depth, Maximum queue size, the number of nodes expanded, time taken by the algorithm.
        """
        return self.depth, self.max_queue_size, self.count_nodes_expanded, self.end_time - self.start_time

    def search(self):
        """
        Perform search and print statistics.

        :return: Return final goal node.
        """
        self.max_queue_size = 0
        self.depth = 0
        self.count_nodes_expanded = 0
        self.start_time = 0
        self.end_time = 0
        self.visited.clear()

        # Perform search based on the algorithm provided. Collect all the statistics while searching.
        final_node = None
        if self.algorithm == UNIFORM_COST:
            self.start_time = time.time()
            final_node = self.general_search(None)
            self.end_time = time.time()
        elif self.algorithm == A_STAR:
            self.start_time = time.time()
            final_node = self.general_search(None)
            self.end_time = time.time()

        # Print the statistics.
        self.print_search_stats(final_node)

        return final_node
