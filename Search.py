from heapq import *

from Board import Board


class Search(object):

    def __init__(self, option, initial_state):
        self.option = option
        self.initial_state = initial_state

    def search(self):
        nodes = []
        visited = []

        # Push the first node into the heap.
        heappush(nodes, (0, Board(self.initial_state, None)))

        while len(nodes) > 0:

            # Pop the cheapest node
            (cost, b) = heappop(nodes)

            # Test for goal state
            if b.is_final_state():
                return b

            # Add the node to the visited state
            visited.append(b)

            # Generate more nodes
            children = b.generate_children(visited)

            # Start adding to the heap
            for child in children:
                heappush(nodes, (1 + cost + child.manhattan_distance(), child))

        # No solution, return.
        return None
