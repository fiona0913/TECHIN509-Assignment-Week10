class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for i, row in enumerate(self.grid):
            print("|".join(row))
            if i < len(self.grid) - 1:
                print("-" * 5)

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player.

        Args:
            row (int): Row index of board
            col (int): Column index of board
            symbol (str): Symbol used by player ('X' or 'O')

        Returns:
            bool: True if the cell is updated, False if the cell is already occupied.
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board.

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner,
                 'Draw' if the game is tied, or 'ongoing' if the game is not yet finished.
        """
        # Check rows for a winner
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        # Check columns for a winner
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != " ":
                return self.grid[0][col]

        # Check diagonals for a winner
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != " ":
            return self.grid[0][2]

        # Check if there are empty cells (game is ongoing)
        for row in self.grid:
            if " " in row:
                return "ongoing"

        # If no winner and no empty cells, it's a draw
        return "Draw"

    def is_full(self) -> bool:
        """
        Check if the current board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != " " for row in self.grid for cell in row)


# Example usage
board = Board()
board.update_board(0, 0, "X")
board.update_board(0, 1, "X")
board.update_board(0, 2, "X")
board.draw_board()

result = board.check_winner()

if result == "X":
    print("X Won")
elif result == "O":
    print("O Won")
elif result == "Draw":
    print("Draw")
elif result == "ongoing":
    print("Ongoing")
