import pygame
from game import Game
from constants import WIDTH, HEIGHT, SQUARE_SIZE

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()  # Crea un'istanza del gioco

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select_piece(row, col)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.move_selected_piece(row, col)

        game.board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()