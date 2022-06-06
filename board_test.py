from board import Board
import unittest


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_get_board(self):
        expected = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n"
        self.assertEqual(expected, self.board.get_board())

    def test_add_cross(self):
        expected = "   | X |   \n-----------\n   |   |   \n-----------\n   |   |   \n"
        self.board.fill_field(" X ", 2)
        self.assertEqual(expected, self.board.get_board())

    def test_add_circle(self):
        expected = "   |   |   \n-----------\n   |   | O \n-----------\n   |   |   \n"
        self.board.fill_field(" O ", 6)
        self.assertEqual(expected, self.board.get_board())
