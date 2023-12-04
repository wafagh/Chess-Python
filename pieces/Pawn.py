from pieces.Piece import Piece
import pygame


class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'imgs/' + color[0] + '_pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'P'


    def get_possible_moves(self,board):

        moves1,moves2,moves3=[],[],[]
        p_moves=[]
        if self.color=='white':
            if self.y-1>=0:
                square=board.get_square_from_pos((self.x,self.y-1))
                square1=board.get_square_from_pos((self.x,self.y-2))
                if square.piece==None:
                    moves1.append(square)
                if self.has_moved==False and square1.piece ==None:
                    moves1.append(board.get_square_from_pos((self.x,self.y-2)))
                p_moves.append(moves1)
            if self.x-1>=0 and self.y-1>=0:
                square=board.get_square_from_pos((self.x-1,self.y-1))
                if square.piece!=None:
                    if square.piece.color=='black':
                        moves2.append(board.get_square_from_pos((self.x-1,self.y-1)))
                        p_moves.append(moves2)
            if self.x+1<=7 and self.y-1>=0:
                square=board.get_square_from_pos((self.x+1,self.y-1))
                if square.piece!=None:
                    if square.piece.color=='black':
                        moves3.append(board.get_square_from_pos((self.x+1,self.y-1)))
                        p_moves.append(moves3)
        elif self.color=='black':
            if self.y+1<=7:
                square=board.get_square_from_pos((self.x,self.y+1))
                square1=board.get_square_from_pos((self.x,self.y+2))
                if square.piece==None:
                    moves1.append(square)
                    if self.has_moved==False and square1.piece ==None:
                        moves1.append(board.get_square_from_pos((self.x,self.y+2)))
                    p_moves.append(moves1)
            if self.x+1<=7 and self.y+1<=7:
                square=board.get_square_from_pos((self.x+1,self.y+1))
                if square.piece!=None:
                    if square.piece.color=='white':
                        moves2.append(board.get_square_from_pos((self.x+1,self.y+1)))
                        p_moves.append(moves2)
            if self.x-1>=0 and self.y+1<=7:
                square=board.get_square_from_pos((self.x-1,self.y+1))
                if square.piece!=None:
                    if square.piece.color=='white':
                        moves3.append(board.get_square_from_pos((self.x-1,self.y+1)))
                        p_moves.append(moves3)
        return p_moves
    
    