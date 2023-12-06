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
                self.check=''
                
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
                        white_moves.extend(v_moves)
                        if len(black_check_squares1)==0:
                              continue
                        else:
                              black_check_squares.extend(black_check_squares1)
                              self.check='black'
                    elif square.piece.color=='black':
                        v_moves,black_check_squares1,white_check_squares1=square.piece.validate_moves(board)
                        black_moves.extend(v_moves)
                        if len(white_check_squares1)==0:
                             continue
                        else:
                              white_check_squares.extend(white_check_squares1)
                              self.check='white'
                        
            return black_moves,white_moves,white_check_squares,black_check_squares
        
        
     

        def check_mate(self,board):
             black_moves,white_moves,white_check_squares,black_check_squares=self.get_moves(board)
             if self.check=='white':
                  
               return True
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
               check=False
               output=[]     
               if self.selected_piece is None:
                    if clicked_square.piece is not None:
                         if clicked_square.piece.color ==self.turn:
                              check,output=self.king_in_check(clicked_square.piece)
                              if check:
                                   self.selected_piece=clicked_square.piece
                              else:
                                   self.selected_piece=None
                                   clicked_square=None

               elif self.selected_piece.color==self.turn and self.selected_piece.move(self, clicked_square):
                    if self.turn=='white':
                         self.turn='black'
                    else:
                         self.turn='white'
                    self.selected_piece=None
                    clicked_square=None

               elif clicked_square.piece is not None:
                    if clicked_square.piece.color == self.turn:
                         check,output=self.king_in_check(clicked_square.piece)
                         if check:
                              self.selected_piece=clicked_square.piece
                         else:
                              self.selected_piece=None
                              clicked_square=None
                    

        def draw(self, display):
            if self.selected_piece is not None:
                self.get_square_from_pos(self.selected_piece.pos).highlight = True
                square1,_,_=self.selected_piece.validate_moves(self)
                for square in square1:
                    square.highlight = True

            for square in self.squares:
                square.draw(display)

        def king_in_check(self,piece):
          black_moves,white_moves,white_check_moves,black_check_moves=self.get_moves(self)
          impos_moves=[]
          pos_moves=[]
          v_moves,b_c_moves,w_c_moves=piece.validate_moves(self)
          if piece.color=='white':
               if white_check_moves:
                    if len(white_check_moves)>1:
                         if piece.notation!='K':
                              return False,impos_moves.append("False")
                         else:
                              for move in v_moves:
                                   for black_move in black_moves:
                                        if black_move==move:
                                             impos_moves.append(move)
                              if len(impos_moves)==0:
                                   return False,impos_moves.append("white")
                              else:
                                   res = [i for i in v_moves if i not in impos_moves]
                                   return True,res
                    else:
                         for move in v_moves:
                              for moves in white_check_moves:
                                   for square1 in moves:
                                        if move==square1:
                                             pos_moves.append(move)
                                        else:
                                             continue
                         if len(pos_moves)==0:
                              return False,impos_moves.append("False")
                         else:
                              return True,pos_moves
               else:
                    return True,v_moves  
          elif piece.color=='black':
               if black_check_moves:
                    if len(black_check_moves)>1:
                         if piece.notation!='K':
                              return False,impos_moves.append("False")
                         else:
                              for move in v_moves:
                                   for white_move in white_moves:
                                        if white_move==move:
                                             impos_moves.append(move)
                              if len(impos_moves)==0:
                                   return False,impos_moves.append("black")
                              else:
                                   res = [i for i in v_moves if i not in impos_moves]
                                   return True,res
                    else:
                         for move in v_moves:
                              for moves in black_check_moves:
                                   for square1 in moves:
                                        if move==square1:
                                             pos_moves.append(move)
                                        else:
                                             continue
                         if len(pos_moves)==0:
                              return False,impos_moves.append("False")
                         else:
                              return True,pos_moves
               else:
                    return True,pos_moves.append("True")          