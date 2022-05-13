from heapq import *

from Board import Board

UNIFORM_COST = 0
A_STAR = 1

MISPLACED_TILE = 0
MANHATTAN_DISTANCE = 1


class Search(object):

    def __init__(self, algorithm, heuristic, initial_state):
        if algorithm != A_STAR and algorithm != UNIFORM_COST:
            exit(-1)
        if algorithm == A_STAR and \
                (heuristic != MANHATTAN_DISTANCE and heuristic != MISPLACED_TILE):
            exit(-1)
        self.algorithm = algorithm
        self.heuristic = heuristic
        self.initial_state = initial_state

    def search(self):
        if self.algorithm == UNIFORM_COST:
            return self.uc_search()
        elif self.algorithm == A_STAR:
            return self.astar_search()

        return None

    def uc_search(self):
        nodes = []
        visited = set()

        # Push the first node into the heap.
        heappush(nodes, (0, Board(self.initial_state, None)))

        while len(nodes) > 0:

            # Pop the cheapest node
            (cost, b) = heappop(nodes)

            # Test for goal state
            if b.is_final_state():
                return b

            # Add the node to the visited state
            visited.add(b)

            # Generate more nodes
            children = b.generate_children(visited)

            # Start adding to the heap
            for child in children:
                heappush(nodes, (1 + cost, child))

        # No solution, return.
        return None

    def astar_search(self):
        nodes = []
        board_start = Board(self.initial_state, None)
        g_x = dict()
        g_x[board_start] = 0
        visited = set()

        # Push the first node into the heap.
        heappush(nodes, (0, board_start))

        while len(nodes) > 0:

            # Pop the cheapest node
            (cost, b) = heappop(nodes)

            if b.is_final_state():
                return b

            # Generate more nodes
            children = b.generate_children(None)

            # Start adding to the heap
            for child in children:

                new_g_x = 1 + g_x[b]
                if child not in g_x.keys():
                    g_x[child] = 100000000

                if new_g_x < g_x[child]:
                    g_x[child] = new_g_x

                    # Get the heuristic cost
                    h_x = 0
                    if self.heuristic == MANHATTAN_DISTANCE:
                        h_x = child.manhattan_distance()
                    elif self.heuristic == MISPLACED_TILE:
                        h_x = child.misplaced_tile()

                    total_cost = g_x[child] + h_x

                    n = (total_cost, child)
                    if n not in visited:
                        heappush(nodes, (total_cost, child))
                        visited.add(n)

        # No solution, return.
        return None
