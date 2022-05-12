from Search import Search

from Board import Board

if __name__ == "__main__":

    s = Search(0, [
        [7, 1, 2],
        [4, 8, 5],
        [6, 3, 0]
    ])
    n = s.search()
    print(Board.get_cost(n.parent))
