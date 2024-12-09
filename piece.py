import pygame
from constants import SQUARE_SIZE, WHITE, BLACK

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False  # Inizialmente non è una dama

    def move(self, row, col):
        """Muove il pezzo nella nuova posizione"""
        self.row = row
        self.col = col

    def promote_to_king(self):
        """Promuove la pedina a dama"""
        self.is_king = True

    def draw(self, win):
        """Disegna il pezzo"""
        color = (255, 255, 255) if self.color == WHITE else (0, 0, 0)
        pygame.draw.circle(win, color, (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)

        if self.is_king:
            pygame.draw.circle(win, (255, 0, 0), (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 4)  # Corona per dama