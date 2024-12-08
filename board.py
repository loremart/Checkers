class Board:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        # 8x8 board with initial piece setup
        board = [[0 for _ in range(8)] for _ in range(8)]
        for row in range(3):  # Set up black pieces
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = -1
        for row in range(5, 8):  # Set up white pieces
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 1
        return board

    def display(self):
        for row in self.grid:
            print(row)