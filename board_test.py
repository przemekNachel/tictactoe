from board import Board
from view import View
import unittest


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def fill_sequence(self, *sequence):
        for number in sequence:
            self.board.fill_field(number)

    def test_get_board(self):
        expected = "   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   \n"
        self.assertEqual(expected, self.board.get_board())

    def test_add_cross(self):
        expected = " O | X |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   \n"
        self.fill_sequence(1, 2)
        self.assertEqual(expected, self.board.get_board())

    def test_add_circle(self):
        expected = "   |   |   \n---+---+---\n   |   | O \n---+---+---\n   |   |   \n"
        self.board.fill_field(6)
        self.assertEqual(expected, self.board.get_board())

    def test_add_circle_to_filled_field(self):
        expected = "   |   |   \n---+---+---\n   | O |   \n---+---+---\n   |   |   \n"
        self.fill_sequence(5, 5)
        self.assertEqual(expected, self.board.get_board())

    def test_winner_circle_top_horizontal(self):
        expected = View.CIRCLE
        self.fill_sequence(1, 4, 2, 5, 3)
        self.assertEqual(expected, self.board.winner)

    def test_winner_cross_left_to_down(self):
        expected = View.CROSS
        self.fill_sequence(2, 1, 3, 4, 6, 7)
        self.assertEqual(expected, self.board.winner)

    def test_winner_circle_left_upper_corner(self):
        expected = View.CIRCLE
        self.fill_sequence(1, 2, 5, 3, 9)
        self.assertEqual(expected, self.board.winner)

    def test_winner_circle_right_upper_corner(self):
        expected = View.CROSS
        self.fill_sequence(1, 3, 2, 5, 6, 7)
        self.assertEqual(expected, self.board.winner)

    def test_no_winner(self):
        expected = None
        self.fill_sequence(5, 7, 2, 8, 9, 1, 4, 6, 3)
        self.assertEqual(expected, self.board.winner)
        self.assertTrue(self.board.end)
