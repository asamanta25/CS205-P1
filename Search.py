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
        g_score = dict()
        g_score[board_start] = 0

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

                new_score = 1 + g_score[b]
                if child not in g_score.keys():
                    g_score[child] = 100000000

                if new_score < g_score[child]:
                    g_score[child] = new_score

                    # Get the heuristic cost
                    heuristic_cost = 0
                    if self.heuristic == MANHATTAN_DISTANCE:
                        heuristic_cost = child.manhattan_distance()
                    elif self.heuristic == MISPLACED_TILE:
                        heuristic_cost = child.misplaced_tile()

                    total_cost = g_score[child] + heuristic_cost

                    heappush(nodes, (total_cost, child))

        # No solution, return.
        return None
