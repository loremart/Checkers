from board import Board
from piece import Piece
from constants import WHITE, BLACK

class Game:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.turn = WHITE  # Inizia con il bianco

    def select_piece(self, row, col):
        """Gestisce la selezione di un pezzo"""
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected_piece = piece
        elif self.selected_piece:
            self.move_selected_piece(row, col)

    def move_selected_piece(self, row, col):
        """Muove il pezzo selezionato sulla scacchiera"""
        if self.selected_piece:
            valid_moves = self.board.get_valid_moves(self.selected_piece)
            if (row, col) in valid_moves:
                self.board.move_piece(self.selected_piece, row, col)
                self.switch_turn()
            self.selected_piece = None

    def switch_turn(self):
        """Cambia il turno"""
        self.turn = WHITE if self.turn == BLACK else BLACK