import pygame


from Square import Square

from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen


class Board:
        def __init__(self, width, height):
                self.width = width
                self.height = height
                self.tile_width = width // 8
                self.tile_height = height // 8
                self.selected_piece = None
                self.turn = 'white'
                
                
                self.config = [
                    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
                ]
                self.squares = self.generate_squares()

                self.setup_board()
        
        def get_moves(self,board):
            black_moves=[]
            white_moves=[]
            black_check_squares=[]
            white_check_squares=[]
            for square in board.squares:
                if square.piece!=None:
                    if square.piece.notation=='K':
                         continue
                    if square.piece.color=='white':
                        v_moves,black_check_squares1,white_check_squares1=square.piece.validate_moves(board)
                        white_moves.append(v_moves)
                        if len(black_check_squares1)==0:
                              continue
                        else:
                              black_check_squares.append(black_check_squares1)
                    elif square.piece.color=='black':
                        v_moves,black_check_squares1,white_check_squares1=square.piece.validate_moves(board)
                        black_moves.append(v_moves)
                        if len(white_check_squares1)==0:
                             continue
                        else:
                              white_check_squares.append(white_check_squares1)
            
            return black_moves,white_moves,white_check_squares,black_check_squares
        
        
        def generate_squares(self):
            output=[]
            for y in range(8):
                for x in range(8):
                    output.append(Square(x,y,self.tile_width,self.tile_height))

            return output
        
        def get_square_from_pos(self,pos):
              for square in self.squares:
                    if (square.x,square.y)==(pos[0],pos[1]):
                        return square
        
        def get_piece_from_pos(self,pos):
              return self.get_square_from_pos(pos).piece
        
        def setup_board(self):
              for y,row in enumerate(self.config):
                    for x,piece in enumerate(row):
                          if piece !='':
                            square=self.get_square_from_pos((x,y))
                            if piece[1]=='R':
                                 square.piece=Rook((x,y),'white' if piece[0]=='w' else 'black',self)
                            elif piece[1]=='N':
                                 square.piece=Knight((x,y),'white' if piece[0]=='w' else 'black',self)
                            elif piece[1]=='B':
                                 square.piece=Bishop((x,y),'white' if piece[0]=='w' else 'black',self)
                            elif piece[1]=='Q':
                                 square.piece=Queen((x,y),'white' if piece[0]=='w' else 'black',self)
                            elif piece[1]=='K':
                                 square.piece=King((x,y),'white' if piece[0]=='w' else 'black',self)
                            elif piece[1]=='P':
                                 square.piece=Pawn((x,y),'white' if piece[0]=='w' else 'black',self)


        def handle_click(self,mx,my):
               x=mx //self.tile_width
               y=my //self.tile_height
               clicked_square=self.get_square_from_pos((x,y))
                    
               if self.selected_piece is None:
                    if clicked_square.piece is not None:
                         if clicked_square.piece.color ==self.turn:
                              self.selected_piece=clicked_square.piece

               elif self.selected_piece.color==self.turn and self.selected_piece.move(self, clicked_square):
                    if self.turn=='white':
                         self.turn='black'
                    else:
                         self.turn='white'
                    self.selected_piece=None
                    clicked_square=None

               elif clicked_square.piece is not None:
                    if clicked_square.piece.color == self.turn:
                         self.selected_piece = clicked_square.piece
                         

        def draw(self, display):
            if self.selected_piece is not None:
                self.get_square_from_pos(self.selected_piece.pos).highlight = True
                square1,_,_=self.selected_piece.validate_moves(self)
                for square in square1:
                    square.highlight = True

            for square in self.squares:
                square.draw(display)