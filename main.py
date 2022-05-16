from search import Search, A_STAR, UNIFORM_COST, MANHATTAN_DISTANCE, MISPLACED_TILE


def check_duplicate_elements(state, size):
    """
    Check for duplicate elements in the state of the board.

    :param state: State of the board.
    :param size: Size of one row of the board.
    :return: Whether the board is valid or not.
    """
    # Check if the same element exists in a different row.
    for i in range(size):
        for j in range(size):
            for k in range(size):
                for m in range(size):
                    if i != k \
                            and j != m \
                            and state[i][j] == state[k][m]:
                        print("Please enter a valid puzzle.")
                        return False

    return True


def validate_row(row, size):
    """
    Check whether the elements entered in one row are valid or not.

    :param row: A list of elements to check.
    :param size: Size of one row.
    :return: Whether the elements are valid or not.
    """
    row_i = []
    for elem in row:

        # Check if it's a valid element.
        i = int(elem)
        if i < 0 or i > 8:
            print("Please enter valid & distinct row elements between 0 & 8.")
            return None

        # Check that there are no duplicate elements
        for j in row_i:
            if i == j:
                print("Please enter valid & distinct row elements between 0 & 8.")
                return None

        row_i.append(i)

    # Check if size number of elements have been entered.
    if len(row_i) != size:
        print("Please enter {} valid row elements.".format(size))
        return None

    return row_i


def get_input():
    """
    Get the input from the user.

    :return: Puzzle, Algorithm & Heuristic
    """
    print("Finding a solution to a provided 8-Puzzle using Uniform Cost Search & A*.")

    algorithm = 0
    state = []
    heuristic = 0

    # Get the algorithm and the heuristic from the user
    while True:
        algorithm = int(input("Please enter the Algorithm (0 - Uniform Cost, 1 - A*): "))

        # Check if algorithm entered is valid or not.
        if algorithm == UNIFORM_COST:
            print("Uniform Cost Algorithm selected.")
            break

        if algorithm != A_STAR:
            print("Please enter valid algorithm.")
            continue

        heuristic = int(input("A* algorithm selected. Please enter heuristic (0 - Misplaced Tile, 1 - Manhattan "
                              "Distance): "))
        # Check if the heuristic entered is correct or not
        if heuristic == MANHATTAN_DISTANCE or heuristic == MISPLACED_TILE:
            break

        print("Please enter valid heuristic.")

    while True:

        # Get the initial state from the user & validate input before searching
        while True:
            row1 = validate_row(input("Enter row 1: ").split(), 3)
            if row1 is not None:
                break

        while True:
            row2 = validate_row(input("Enter row 2: ").split(), 3)
            if row2 is not None:
                break

        while True:
            row3 = validate_row(input("Enter row 3: ").split(), 3)
            if row3 is not None:
                break

        # Need to convert from string to int
        row1 = [int(i) for i in row1]
        row2 = [int(i) for i in row2]
        row3 = [int(i) for i in row3]

        # Check if there are duplicate elements in the whole board
        state = [row1, row2, row3]
        if check_duplicate_elements(state, 3):
            break

    return state, algorithm, heuristic


if __name__ == "__main__":
    puzzle, a, h = get_input()
    s = Search(a, h, puzzle)
    n = s.search()
