from board import Board
from constants import WHITE, BLACK

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = WHITE
        self.selected_piece = None
        self.winner = None

    def switch_turn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected_piece = piece
            return True
        self.selected_piece = None
        return False

    def move_selected_piece(self, new_row, new_col):
        if not self.selected_piece:
            return False

        if self.board.is_valid_move(self.selected_piece, new_row, new_col):
            self.board.move(self.selected_piece, new_row, new_col)

            # Gestione catture
            captured = self.board.check_capture(self.selected_piece, new_row, new_col)
            if captured:
                self.board.remove_captured_pieces(captured)

            # Passa al turno successivo
            self.switch_turn()
            self.selected_piece = None
            return True

        # Se la mossa non è valida, il pezzo resta selezionato
        return False

    def check_winner(self):
        if not self.board.has_pieces(WHITE):
            self.winner = BLACK
        elif not self.board.has_pieces(BLACK):
            self.winner = WHITE
        return self.winner