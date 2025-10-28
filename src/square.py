
class square:
    def __init__(self, row, col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece is not None

    
    def has_friend(self, color):
        return self.has_piece() and self.piece.color == color
    
    def has_rival(self, color):
        return self.has_piece() and self.piece.color != color

    def isempty_or_rivel(self, color):
        return self.is_empty() or self.has_rival(color)
    
    def is_empty(self):
        return not self.has_piece()

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True