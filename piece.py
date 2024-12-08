class Piece:
    def __init__(self, color, is_king=False):
        self.color = color  # 1 for white, -1 for black
        self.is_king = is_king

    def make_king(self):
        self.is_king = True