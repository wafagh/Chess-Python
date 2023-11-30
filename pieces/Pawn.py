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

        moves=[]
        if self.color=='white':
            if self.x-1>=0:
                moves.append(board.get_square_from_pos((self.x-1,self.y)))
            if self.has_moved==False:
                moves.append(board.get_square_from_pos((self.x-2,self.y)))

            if self.x-1>=0 and self.y-1>=0:
                square=board.get_square_from_pos((self.x-1,self.y-1))
                if square.piece!=None:
                    if square.piece.color=='black':
                        moves.append(board.get_square_from_pos((self.x-1,self.y-1)))
            if self.x-1>=0 and self.y+1<=7:
                square=board.get_square_from_pos((self.x-1,self.y+1))
                if square.piece!=None:
                    if square.piece.color=='black':
                        moves.append(board.get_square_from_pos((self.x-1,self.y+1)))

        elif self.color=='black':
            if self.x+1<=7:
                moves.append(board.get_square_from_pos((self.x+1,self.y)))
            if self.has_moved==False:
                moves.append(board.get_square_from_pos((self.x+2,self.y)))

            if self.x+1<=7 and self.y-1>=0:
                square=board.get_square_from_pos((self.x+1,self.y-1))
                if square.piece!=None:
                    if square.piece.color=='white':
                        moves.append(board.get_square_from_pos((self.x+1,self.y-1)))
            if self.x+1<=7 and self.y+1<=7:
                square=board.get_square_from_pos((self.x+1,self.y+1))
                if square.piece!=None:
                    if square.piece.color=='white':
                        moves.append(board.get_square_from_pos((self.x+1,self.y+1)))

        return moves
    
    