import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        # 初始化一个棋盘实例，用于所有测试
        self.board = Board()

    def test_row_winner(self):
        # 测试行胜利
        self.board.grid = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_column_winner(self):
        # 测试列胜利
        self.board.grid = [
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_diagonal_winner_main(self):
        # 测试主对角线胜利
        self.board.grid = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_diagonal_winner_anti(self):
        # 测试反对角线胜利
        self.board.grid = [
            [" ", "O", "X"],
            ["O", "X", " "],
            ["X", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_no_winner(self):
        # 测试没有赢家
        self.board.grid = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertEqual(self.board.check_winner(), "")

if __name__ == "__main__":
    unittest.main()
