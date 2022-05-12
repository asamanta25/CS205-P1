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
        self.state = state
        self.children = []
        self.board_size = len(self.state)
        self.parent = parent

        self.empty_row = -1
        self.empty_col = -1

        # Get empty board position
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.state[row][col] == 0:
                    self.empty_row = row
                    self.empty_col = col

        self.valid_positions = []

    def __eq__(self, other):
        return self.state == other.board

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return True

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
        Get surrounding positions for the position passed.

        :return:
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

        :return:
        """
        if len(self.children) != 0:
            return self.children

        self.get_surrounding_valid_positions()

        # Swap the blank space with the valid positions that we previously got.
        for position in self.valid_positions:
            b = copy.deepcopy(self.state)
            row, col = position
            b[self.empty_row][self.empty_col] = b[row][col]
            b[row][col] = 0
            if self.parent and self.parent.state == b:
                continue

            # Check if a board has already been visited
            found = False
            for node in visited:
                if node.state == b:
                    found = True

            # Only add to the set of children if Node was not
            # visited earlier.
            if not found:
                self.children.append(Board(b, self))

        return self.children

    def is_final_state(self):
        """
        Check if the current board is the final solved state of the Board.

        :return: Boolean indicating whether Board is the final state or not.
        """
        return self.state == Board.final

    def misplaced_tile(self):
        """
        Return the number of misplaced tiles from the final state of the Board.

        :return: The number of tiles that are misplaced.
        """
        count = 0
        for row in range(self.board_size):
            for col in range(self.board_size):

                # Increment count only if Board position is not an empty position
                if (row != self.empty_row and col != self.empty_col) \
                        and (self.state[row][col] != Board.final[row][col]):
                    count = count + 1

        return count

    def manhattan_distance(self):
        """
        Return the Manhattan distance of the board from the final solved state.

        :return: The Manhattan distance.
        """
        manhattan_distance = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                r = -1
                c = -1
                k = self.state[row][col]
                if k == 0:
                    continue
                if k % self.board_size == 0:
                    r = (k / self.board_size) - 1
                    c = self.board_size - 1
                else:
                    r = int(k / self.board_size)
                    c = (k % self.board_size) - 1

                manhattan_distance = manhattan_distance + abs(r - row) + abs(c - col)
        return manhattan_distance

    @property
    def board(self):
        return self.state

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
