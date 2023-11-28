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
             x=mx
             y=my
             clicked_square=self.get_square_from_pos((x,y))

             if self.selected_piece is None:
                  if clicked_square.piece is not None:
                       if clicked_square.piece.color ==self.turn:
                            self.selected_piece=clicked_square.piece
                       

              

        def draw(self, display):
            if self.selected_piece is not None:
                self.get_square_from_pos(self.selected_piece.pos).highlight = True
                for square in self.selected_piece.get_valid_moves(self):
                    square.highlight = True

            for square in self.squares:
                square.draw(display)