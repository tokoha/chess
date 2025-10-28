import pygame

from dragger import Dragger
from const import *
from move import Move
from board import Board


class Game:

    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()



    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light Green
                else:
                    color = (119, 154, 88) # Dark Green


                rect = (col * SqSIZE, row * SqSIZE, SqSIZE, SqSIZE)

                pygame.draw.rect(surface, color, rect) 
    
    
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                
                if self.board.squares[row][col].has_piece():
                    
                    
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SqSIZE + SqSIZE // 2, row * SqSIZE + SqSIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)
    

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                #color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                #rect
                rect = (move.final.col * SqSIZE, move.final.row * SqSIZE, SqSIZE, SqSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)