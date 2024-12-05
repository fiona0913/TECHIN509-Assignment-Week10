import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_row_winner(self):
        self.board.grid = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(self.board.check_winner(), "X")

    def test_column_winner(self):
        self.board.grid = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
        self.assertEqual(self.board.check_winner(), "O")

    def test_diagonal_winner(self):
        self.board.grid = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(self.board.check_winner(), "X")

    def test_draw(self):
        self.board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertEqual(self.board.check_winner(), "Draw")

    def test_ongoing(self):
        self.board.grid = [["X", "O", " "], ["O", "X", " "], [" ", " ", " "]]
        self.assertEqual(self.board.check_winner(), "ongoing")


if __name__ == "__main__":
    unittest.main()
