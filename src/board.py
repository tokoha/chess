from const import *
from square import square
from piece import *
from move import Move
class Board:

    def __init__(self):
        self.squares =  [[0, 0, 0, 0, 0, 0, 0, 0,] for col in range(COLS)] 

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    def calc_moves(self, piece, row, col):
        '''calculates all possible moves for a piece'''
        def knight_moves():
            possible_moves={
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
            }

            for possible_moves in possible_moves:
                [possible_moves_row, possible_moves_col] = possible_moves

                if square.in_range(possible_moves_row, possible_moves_col):
                    if self.squares[possible_moves_row][possible_moves_col].isempty_or_rivel(piece.color):
                        # create squares of the  move
                        initial = square(row, col)
                        final = square(possible_moves_row, possible_moves_col) #piece = piece

                        #move
                        move = Move(initial, final)
                        piece.add_move(move)
        
        def pawn_moves():
        
            steps = 1  if piece.moves else 2
            
            #vectical moves
            start = row + piece.dir
            end = row + (piece.dir * (steps + 1))

            for move_row in range(start, end, piece.dir):
                if square.in_range(move_row):
                    if self.squares[move_row][col].is_empty():
                        # create inital and final squares
                        initial = square(move_row, col)
                        final = square(move_row, col)

                        #create move
                        move = Move(initial, final)
                        piece.add_move(move)
                    #blocked
                    else: break
                #out of range
                else: break
            #diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival(piece.color):
                        # create squares of the  move
                        initial = square(row, col)
                        final = square(possible_move_row, possible_move_col) #piece = piece

                        #move
                        move = Move(initial, final)
                        piece.add_move(move)
            
        def straightLine_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
            
                while True:
                    if square.in_range(possible_move_row, possible_move_col):
                        #create squares of the move
                        initial = square(row, col)
                        final = square(possible_move_row, possible_move_col)
                        
                        move = Move(initial, final)
                        
                        #empty square
                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            piece.add_move(move)
                        
                        if self.squares[possible_move_row][possible_move_col].has_friend(piece.color):
                            break
                        
                        #rival piece on square
                        if self.squares[possible_move_row][possible_move_col].has_rival(piece.color):
                            piece.add_move(move)
                            break
                    else:
                        break
            
            
                    
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr



        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straightLine_moves({
                (-1, -1), # up left
                (-1, 1), # up right
                (1, -1), # down left
                (1, 1)# down right 
            })

        elif isinstance(piece, Rook):
            straightLine_moves({
                (-1, 0), # up
                (1, 0), # down
                (0, -1), # left
                (0, 1) # right
            })

        elif isinstance(piece, Queen):
            straightLine_moves({
                (-1, -1), # up left
                (-1, 1), # up right
                (1, -1), # down left
                (1, 1), # down right 
                (-1, 0), # up
                (1, 0), # down
                (0, -1), # left
                (0, 1) # right
            })

        elif isinstance(piece, King):
            straightLine_moves()







    def _create(self):
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = square(row, col)

    def _add_pieces(self, color):
        row_pawn = 6 if color == 'white' else 1
        row_other = 7 if color == 'white' else 0
        
        for col in range(COLS):
            self.squares[row_pawn][col] = square(row_pawn, col, Pawn(color))

        #Knights
        self.squares[row_other][1] = square(row_other, 1, Knight(color))
        self.squares[row_other][6] = square(row_other, 6, Knight(color))


        #Bishops
        self.squares[row_other][2] = square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = square(row_other, 5, Bishop(color))
        

        #Rooks
        self.squares[row_other][0] = square(row_other, 0, Rook(color))
        self.squares[row_other][7] = square(row_other, 7, Rook(color))

        #Queen
        self.squares[row_other][3] = square(row_other, 3, Queen(color))
        #King
        self.squares[row_other][4] = square(row_other, 4, King(color))