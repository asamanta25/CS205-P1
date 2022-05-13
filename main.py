from Search import Search, A_STAR

from Board import Board


if __name__ == "__main__":

    algorithm = int(input("Please enter the Algorithm (0 - Uniform Cost, 1 - A*): "))
    heuristic = 0
    if algorithm == A_STAR:
        heuristic = int(input("A* algorithm selected. Please enter heuristic (0 - Misplaced Tile, 1 - Manhattan "
                              "Distance): "))
    else:
        print("Uniform Cost Algorithm selected.")

    s = Search(algorithm, heuristic, [
            [0, 7, 2],
            [4, 6, 1],
            [3, 5, 8]
        ]
    )
    n = s.search()
    print(Board.get_cost(n.parent))
