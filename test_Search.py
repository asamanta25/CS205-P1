from unittest import TestCase

from Search import Search


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
    ]

    def test_search(self):
        for test_case in TestSearch.TESTS:
            (test_board, test_depth) = test_case
            s = Search(0, test_board)
            assert s.search() == test_depth
