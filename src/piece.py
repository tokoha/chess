import os

class piece:
    def __init__(self, name, color, value, texture= None, texture_rect = None):
            self.name = name
            self.color = color
            self.moves = []
            value_sign = 1 if color == 'white' else -1
            self.value = value  * value_sign
            self.set_texture()
            self.texture_rect = texture_rect


    def set_texture(self,size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def add_move(self, move):
        self.moves.append(move)
        

class Pawn(piece):
    def __init__(self, color):
            self.dir = -1 if color == 'white' else 1 #white moves up, black moves down
            super().__init__('pawn', color, 1.0)

class Knight(piece):
    def __init__(self, color):
            super().__init__('knight', color, 3.0)

class Bishop(piece):
    def __init__(self, color):
            super().__init__('Bishop', color, 3.0001)

class Rook(piece):
    def __init__(self, color):
            super().__init__('Rook', color, 5.0)

class Queen(piece):
    def __init__(self, color):
            super().__init__('Queen', color, 9.0)

class King(piece):
    def __init__(self, color):
            super().__init__('king', color, 100000.0)