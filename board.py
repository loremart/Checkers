# board.py
import pygame
from constants import WHITE, BLACK, RED, ROWS, COLS, SQUARE_SIZE
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))  # Pedine rosse
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))  # Pedine bianche
                    else:
                        self.board[row].append(0)  # Caselle vuote
                else:
                    self.board[row].append(0)  # Caselle vuote

    def draw_squares(self, win):
        win.fill(BLACK)  # Pulisce lo schermo con il colore nero
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col] = 0
        self.board[row][col] = piece
        piece.row = row
        piece.col = col

    def get_valid_moves(self, piece):
        # Questo è solo un esempio semplice per i movimenti base
        valid_moves = []
        direction = -1 if piece.color == WHITE else 1
        for r in range(piece.row + direction, piece.row + 2 * direction, direction):
            for c in range(piece.col - 1, piece.col + 2, 2):
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if self.board[r][c] == 0:
                        valid_moves.append((r, c))
        return valid_moves