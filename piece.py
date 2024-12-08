# piece.py
import pygame
from constants import WHITE, RED, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - 10
        pygame.draw.circle(win, self.color,
                           (self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                            self.row * SQUARE_SIZE + SQUARE_SIZE // 2), radius)

        if self.king:
            pygame.draw.circle(win, (255, 255, 0),
                               (self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                self.row * SQUARE_SIZE + SQUARE_SIZE // 2), radius // 2)