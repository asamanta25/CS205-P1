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

                heuristic_cost = 0
                # Get the heuristic cost if algorithm is A*
                if self.algorithm == A_STAR:
                    if self.heuristic == MANHATTAN_DISTANCE:
                        heuristic_cost = child.manhattan_distance()
                    else:
                        heuristic_cost = child.misplaced_tile()

                heappush(nodes, (1 + cost + heuristic_cost, child))

        # No solution, return.
        return None
