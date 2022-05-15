import copy


class Board(object):

    """
    Final position of the board.
    """
    final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, state, parent):
        # Heuristics parameters
        self.m_dist = -1
        self.m_tile_count = -1

        # Node parameters
        self._parent = parent
        self._hash = None
        self._cost = 0
        self._depth = 0
        self._state = state
        self.children = []
        self.board_size = len(self.state)

        # Get empty board position
        self.empty_row = -1
        self.empty_col = -1
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.state[row][col] == 0:
                    self.empty_row = row
                    self.empty_col = col

        self.valid_positions = []

    def __eq__(self, other):
        """
        Overload the == operator. Compare whether one board is equal to
        another board or not.

        :param other: The board to be compared with.
        :return: Whether the 2 boards are equal nor not.
        """
        return self.state == other.state

    def __lt__(self, other):
        """
        Check if one board is less than another board. The cost of the board needs to be considered.

        :param other: The board to be compared with.
        :return: Whether one board is less than another one.
        """

        # Need to compare the costs. If the cost and the boards are the same, the depth needs to be compared.
        if (self.cost == other.cost) and (self.state == other.state):
            return self.depth < other.depth
        return self.cost < other.cost

    def __hash__(self):
        """
        Compute a hash value of the board. This is needed because a set can't hash iterable objects and
        list is an iterable object.

        :return: A hash value of the board.
        """
        if self._hash is None:
            k = []
            # Convert each row into a tuple and then create a tuple of tuples where each tuple is a row.
            # Return the has. This conversion is required because the hash function can't work with lists.
            for i in self.state:
                k.append(tuple(i))
            self._hash = hash(tuple(k))
        return self._hash

    def print_board(self):
        """
        Print the board.

        :return: None
        """
        for row in self.state:
            print(row)

    def print_children(self):
        """
        Print the children.

        :return: None
        """

        for child in self.children:
            child.print_board()
            print("\n")

    def get_surrounding_valid_positions(self):
        """
        Get surrounding positions for the position passed. Collect the valid positions for a board.
        Considering that (i, j) is position of the missing tile on the board, the only valid positions would be
        (i - 1, j), (i + 1, j), (i, j - 1) and (i, j + 1). If the boundaries are kept in check, it can be observed that
        all the valid positions are either in the missing tile row or in the missing tile column. The for loop bellow
        collects all the positions that either are in the missing tile row or in the missing tile column.

        :return: A list of valid positions.
        """

        # row + 2 & col + 2 because range will then return values up to row + 1
        for i in range(self.empty_row - 1, self.empty_row + 2):
            if i < 0 or i >= self.board_size:
                continue
            for j in range(self.empty_col - 1, self.empty_col + 2):
                if j < 0 or j >= self.board_size:
                    continue
                is_empty_row = self.empty_row == i
                is_empty_col = self.empty_col == j
                if is_empty_row ^ is_empty_col == 1:
                    self.valid_positions.append((i, j))

        return self.valid_positions

    def generate_children(self, visited):
        """
        Generate the children for the current puzzle.

        :return: the list of children.
        """
        if len(self.children) != 0:
            return self.children

        # Get the valid positions where the missing tile could be
        self.get_surrounding_valid_positions()

        # Swap the blank space with the valid positions previously obtained.
        for position in self.valid_positions:
            b = copy.deepcopy(self._state)
            row, col = position
            b[self.empty_row][self.empty_col] = b[row][col]
            b[row][col] = 0

            # if self.parent and self.parent.state == b:
            #     continue

            # Check if a board has already been visited
            child = Board(b, self)
            child.depth = 1 + self.depth
            found = False
            if visited is not None:
                found = child in visited

            # Only add to the set of children if Node was not
            # visited earlier.
            if not found:
                self.children.append(child)

        return self.children

    def goal_test(self, state):
        """
        Check if the current board is the final solved state of the Board.

        :return: Boolean indicating whether Board is the final state or not.
        """
        return self._state == Board.final

    def misplaced_tile(self):
        """
        Return the number of misplaced tiles from the final state of the Board.

        :return: The number of tiles that are misplaced.
        """
        if self.m_tile_count != -1:
            return self.m_tile_count

        # Iterate over the final board and the current board and check which tiles are misplaced.
        self.m_tile_count = 0
        for row in range(self.board_size):
            for col in range(self.board_size):

                # Increment count only if Board position is not an empty position
                if (self._state[row][col] != 0) \
                        and (self._state[row][col] != Board.final[row][col]):
                    self.m_tile_count = self.m_tile_count + 1

        return self.m_tile_count

    def manhattan_distance(self):
        """
        Return the Manhattan distance of the board from the final solved state.

        :return: The Manhattan distance.
        """
        if self.m_dist != -1:
            return self.m_dist

        # For each of the misplaced tiles, just need to take the absolute difference between the
        # rows and the columns and add them up.
        self.m_dist = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                r = -1
                c = -1
                k = self._state[row][col]
                if k == 0:
                    continue
                if k % self.board_size == 0:
                    r = (k / self.board_size) - 1
                    c = self.board_size - 1
                else:
                    r = int(k / self.board_size)
                    c = (k % self.board_size) - 1

                self.m_dist = self.m_dist + abs(r - row) + abs(c - col)
        return self.m_dist

    # Properties of this class
    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @staticmethod
    def print_board_from_initial_state(board):
        """
        Print the board states from the beginning to the end.

        :param board: Board to print.
        :return: None
        """
        if board is None:
            return

        # Print the board states higher up in the Tree first
        Board.print_board_from_initial_state(board.parent)
        board.print_board()

    @staticmethod
    def get_depth(board):
        """
        Get the cost of a solved state recursively by adding 1 to the cost
        until the root node is reached.

        :param board: Board for which cost is required.
        :return: 1 + the cost of the parent node.
        """
        if board is None:
            return 0

        return 1 + Board.get_depth(board.parent)

    @staticmethod
    def get_board_for_size(size):
        """
        Create a solved board based on the size provided. Ex - if size = 5, return a solved 24-Puzzle.

        :param size: No. of elements in one row.
        :return: A solved N-Puzzle.
        """
        for i in size:
            for j in size:
                Board.final[i][j] = (i * size) + j + 1
