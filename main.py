# main.py
import pygame
from board import Board
from constants import WIDTH, HEIGHT, SQUARE_SIZE

def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco della Dama")

    board = Board()
    selected_piece = None
    valid_moves = {}

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE

                if selected_piece:
                    if (row, col) in valid_moves:
                        board.move_piece(selected_piece, row, col)
                        selected_piece = None
                        valid_moves = {}
                    else:
                        selected_piece = None
                        valid_moves = {}
                else:
                    piece = board.get_piece(row, col)
                    if piece != 0:
                        selected_piece = piece
                        valid_moves = board.get_valid_moves(piece)

        # Disegna la scacchiera
        board.draw(WIN)

        # Disegna i movimenti validi (cerchi verdi)
        for move in valid_moves:
            r, c = move
            pygame.draw.circle(WIN, (0, 255, 0),
                               (c * SQUARE_SIZE + SQUARE_SIZE // 2,
                                r * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()