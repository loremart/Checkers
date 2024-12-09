import pygame
from constants import WHITE, BLACK, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def move(self, row, col):
        self.row = row
        self.col = col

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - 10
        x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
        color = (255, 255, 255) if self.color == WHITE else (0, 0, 0)
        pygame.draw.circle(win, color, (x, y), radius)