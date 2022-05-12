from unittest import TestCase

from Board import Board

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

    def test_manhattan_distance(self):
        b = Board(Board.final, None)
        assert b.manhattan_distance() == 0

        b2 = Board([
            [5, 0, 8],
            [4, 2, 1],
            [7, 3, 6]
        ], None)
        assert b2.manhattan_distance() == 13
