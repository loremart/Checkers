import pygame
from piece import Piece
from constants import SQUARE_SIZE, WHITE, BLACK

class Board:
    def __init__(self):
        self.board = self.create_board()
        self.selected_piece = None
        self.turn = WHITE  # Il turno inizia con il bianco

    @staticmethod
    def create_board():
        """Crea la scacchiera e posiziona i pezzi iniziali"""
        board = [[None for _ in range(8)] for _ in range(8)]  # 8x8 scacchiera vuota
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 != 0:  # Pezzi vengono messi solo nelle case scure
                    if row < 3:  # Pezzi neri
                        board[row][col] = Piece(row, col, BLACK)
                    elif row > 4:  # Pezzi bianchi
                        board[row][col] = Piece(row, col, WHITE)
        return board

    def get_piece(self, row, col):
        """Restituisce il pezzo nella posizione data (row, col)"""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None

    def is_valid_move(self, piece, new_row, new_col):
        """Controlla se la mossa è valida per un dato pezzo"""
        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            return False  # Fuori dalla scacchiera

        if self.board[new_row][new_col] is not None:
            return False  # Casella già occupata

        row_diff = abs(piece.row - new_row)
        col_diff = abs(piece.col - new_col)

        # Se è una mossa semplice (diagonale)
        if row_diff == 1 and col_diff == 1:
            if piece.color == WHITE and new_row < piece.row:  # Le pedine bianche non possono tornare indietro
                return False
            if piece.color == BLACK and new_row > piece.row:  # Le pedine nere non possono tornare indietro
                return False
            return True

        # Movimento con cattura (2 caselle)
        if row_diff == 2 and col_diff == 2:
            middle_row = (piece.row + new_row) // 2
            middle_col = (piece.col + new_col) // 2
            middle_piece = self.get_piece(middle_row, middle_col)

            if middle_piece and middle_piece.color != piece.color:  # Cattura un pezzo avversario
                return True

        return False

    def move_piece(self, piece, new_row, new_col):
        """Muove un pezzo dalla posizione attuale alla nuova posizione"""
        row_diff = abs(piece.row - new_row)
        col_diff = abs(piece.col - new_col)

        # Se c'è una cattura
        if row_diff == 2 and col_diff == 2:
            middle_row = (piece.row + new_row) // 2
            middle_col = (piece.col + new_col) // 2
            middle_piece = self.get_piece(middle_row, middle_col)

            if middle_piece:  # Se c'è un pezzo nemico nel mezzo, lo rimuoviamo
                self.board[middle_row][middle_col] = None

        # Muove il pezzo sulla nuova posizione
        self.board[piece.row][piece.col] = None  # Rimuove il pezzo dalla vecchia posizione
        self.board[new_row][new_col] = piece  # Posiziona il pezzo nella nuova posizione
        piece.move(new_row, new_col)  # Aggiorna la posizione del pezzo

        # Promuove la pedina a dama se raggiunge l'estremità della scacchiera
        if piece.color == WHITE and new_row == 0:
            piece.promote_to_king()
        elif piece.color == BLACK and new_row == 7:
            piece.promote_to_king()

        # Cambia il turno
        self.turn = WHITE if self.turn == BLACK else BLACK

    def get_valid_moves(self, piece):
        """Restituisce tutte le mosse valide per un dato pezzo"""
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonali

        for drow, dcol in directions:
            new_row = piece.row + drow
            new_col = piece.col + dcol

            # Movimento semplice (1 casella)
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.board[new_row][new_col] is None:
                    moves.append((new_row, new_col))

            # Movimento con cattura (2 caselle)
            capture_row = piece.row + 2 * drow
            capture_col = piece.col + 2 * dcol
            if 0 <= capture_row < 8 and 0 <= capture_col < 8:
                middle_row = piece.row + drow
                middle_col = piece.col + dcol
                middle_piece = self.get_piece(middle_row, middle_col)

                if middle_piece and middle_piece.color != piece.color and self.board[capture_row][capture_col] is None:
                    moves.append((capture_row, capture_col))

        return moves

    def draw(self, win):
        """Disegna la scacchiera e i pezzi"""
        win.fill((0, 0, 0))  # Colore di sfondo

        # Disegna la scacchiera
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (128, 128, 128)
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Disegna i pezzi solo se sono validi
        for row in self.board:
            for piece in row:
                if piece:  # Verifica se il pezzo è valido (non None)
                    piece.draw(win)