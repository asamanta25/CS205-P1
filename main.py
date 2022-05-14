from Board import Board
from Search import Search, A_STAR

def get_input():
    print("Finding a solution to a provided 8-Puzzle using Uniform Cost Search & A*.")
    algorithm = int(input("Please enter the Algorithm (0 - Uniform Cost, 1 - A*): "))
    heuristic = 0
    if algorithm == A_STAR:
        heuristic = int(input("A* algorithm selected. Please enter heuristic (0 - Misplaced Tile, 1 - Manhattan "
                              "Distance): "))
    else:
        print("Uniform Cost Algorithm selected.")

    row1 = input("Enter row 1: ").split()
    row2 = input("Enter row 2: ").split()
    row3 = input("Enter row 3: ").split()

    row1 = [int(i) for i in row1]
    row2 = [int(i) for i in row2]
    row3 = [int(i) for i in row3]

    return [row1, row2, row3]


if __name__ == "__main__":

    s = Search(1, 1, [
                [0, 7, 2],
                [4, 6, 1],
                [3, 5, 8]
            ])# get_input())

    n = s.general_search(None)
    print(Board.get_cost(n.parent))
