class Board:
    def __init__(self):
        # 初始化 3x3 棋盘，所有格子初始为空格
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game with appropriate borders.
        """
        size = len(self.grid)  # 获取棋盘大小
        for i in range(size):
            # 打印分隔线
            print(" ---" * size)
            # 打印每行内容，添加边框
            print("| " + " | ".join(self.grid[i]) + " |")
        # 打印最后一条分隔线
        print(" ---" * size)

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player.

        Args:
            row (int): Row index of the board.
            col (int): Column index of the board.
            symbol (str): Symbol used by the player ('X' or 'O').

        Returns:
            bool: True if the cell is updated successfully, False otherwise.
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board.

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string.
        """
        # Check rows and columns
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ":
                return self.grid[i][0]  # Row winner
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return self.grid[0][i]  # Column winner

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]  # Main diagonal winner
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]  # Anti-diagonal winner

        return ""  # No winner

    def is_full(self) -> bool:
        """
        Check if the current board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != " " for row in self.grid for cell in row)
