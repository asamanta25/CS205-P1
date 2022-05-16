from unittest import TestCase

from board import Board


class TestBoard(TestCase):
    def test_get_surrounding_valid_positions(self):
        self.fail()

    def test_generate_children(self):
        self.fail()

    def test_is_final_state(self):
        self.fail()

    def test_misplaced_tile(self):
        b = Board(Board.final, None)
        assert b.misplaced_tile() == 0

        b2 = Board([
            [5, 0, 8],
            [4, 2, 1],
            [7, 3, 6]
        ], None)

        assert b2.misplaced_tile() == 6

        b = Board([
            [0, 1, 2],
            [4, 5, 3],
            [7, 8, 6]
        ], None)
        assert b.misplaced_tile() == 4

    def test_manhattan_distance(self):
        b = Board(Board.final, None)
        assert b.manhattan_distance() == 0

        b2 = Board([
            [5, 0, 8],
            [4, 2, 1],
            [7, 3, 6]
        ], None)
        assert b2.manhattan_distance() == 13

        b2 = Board([
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ], None)
        assert b2.manhattan_distance() == 1

        b2 = Board([
            [7, 2, 4],
            [5, 0, 6],
            [8, 3, 1]
        ], None)
        assert b2.manhattan_distance() == 14

    def test_get_surrounding_valid_positions(self):
        b = Board([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ], None)
        valid_positions = [(1, 2), (2, 1)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ], None)
        valid_positions = [(1, 1), (2, 0), (2, 2)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 3],
            [4, 5, 6],
            [0, 7, 8]
        ], None)
        valid_positions = [(1, 0), (2, 1)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 3],
            [0, 5, 6],
            [4, 7, 8]
        ], None)
        valid_positions = [(0, 0), (1, 1), (2, 0)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 3],
            [4, 0, 6],
            [7, 5, 8]
        ], None)
        valid_positions = [(0, 1), (1, 0), (1, 2), (2, 1)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
        ], None)
        valid_positions = [(0, 2), (1, 1), (2, 2)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 2, 0],
            [4, 5, 3],
            [7, 8, 6]
        ], None)
        valid_positions = [(0, 1), (1, 2)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [1, 0, 2],
            [4, 5, 3],
            [7, 8, 6]
        ], None)
        valid_positions = [(0, 0), (0, 2), (1, 1)]
        assert b.get_surrounding_valid_positions() == valid_positions

        b = Board([
            [0, 1, 2],
            [4, 5, 3],
            [7, 8, 6]
        ], None)
        valid_positions = [(0, 1), (1, 0)]
        assert b.get_surrounding_valid_positions() == valid_positions
