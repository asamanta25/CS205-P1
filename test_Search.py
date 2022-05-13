from unittest import TestCase

from Board import Board
from Search import Search, A_STAR, UNIFORM_COST, MANHATTAN_DISTANCE, MISPLACED_TILE


class TestSearch(TestCase):

    TESTS = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ],
            0
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [0, 7, 8]
            ],
            2
        ),
        (
            [
                [1, 2, 3],
                [5, 0, 6],
                [4, 7, 8]
            ],
            4
        ),
        (
            [
                [1, 3, 6],
                [5, 0, 2],
                [4, 7, 8]
            ],
            8
        ),
        (
            [
                [1, 3, 6],
                [5, 0, 7],
                [4, 8, 2]
            ],
            12
        ),
        (
            [
                [1, 6, 7],
                [5, 0, 3],
                [4, 8, 2]
            ],
            16
        ),
        (
            [
                [7, 1, 2],
                [4, 8, 5],
                [6, 3, 0]
            ],
            20
        ),
        (
            [
                [0, 7, 2],
                [4, 6, 1],
                [3, 5, 8]
            ],
            24
        )
    ]

    TESTS_NO_SOLUTION = [
        [
            [8, 1, 2],
            [0, 4, 3],
            [7, 6, 5]
        ]
    ]

    def search(self, algorithm, heuristic):
        # Test cases that can be solved
        for test_case in TestSearch.TESTS:
            (test_board, test_depth) = test_case
            s = Search(algorithm, heuristic, test_board)
            b = s.search()
            assert b is not None
            assert Board.get_cost(b.parent) == test_depth

        # Test cases that can't be solved
        for test_case in TestSearch.TESTS_NO_SOLUTION:
            s = Search(algorithm, heuristic, test_case)
            b = s.search()
            assert b is None

    def test_uc_search(self):
        self.search(UNIFORM_COST, 0)

    def test_a_star_manhattan_distance_search(self):
        for test_case in TestSearch.TESTS:
            (test_board, test_depth) = test_case
            s = Search(A_STAR, MANHATTAN_DISTANCE, test_board)
            b = s.search()
            assert b is not None
            assert Board.get_cost(b.parent) == test_depth

    def test_a_star_misplaced_tile_search(self):
        for test_case in TestSearch.TESTS:
            (test_board, test_depth) = test_case
            s = Search(A_STAR, MISPLACED_TILE, test_board)
            b = s.search()
            assert b is not None
            assert Board.get_cost(b.parent) == test_depth
