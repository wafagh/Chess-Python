from pieces.Piece import Piece
import pygame


class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'imgs/' + color[0] + '_knight.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'N'



    def get_possible_moves(self,board):
        moves1,moves2,moves3,moves4,moves5,moves6,moves7,moves8=[],[],[],[],[],[],[],[]
        p_moves=[]
        if self.x +2 <=7:
            if self.y +1 <=7:
                moves1.append(board.get_square_from_pos((self.x+2,self.y+1)))
                p_moves.append(moves1)
            if self.y-1 >=0:
                moves2.append(board.get_square_from_pos((self.x+2,self.y-1)))
                p_moves.append(moves2)

        if self.x-2>=0:
            if self.y +1 <=7:
                moves3.append(board.get_square_from_pos((self.x-2,self.y+1)))
                p_moves.append(moves3)
            if self.y-1 >=0:
                moves4.append(board.get_square_from_pos((self.x-2,self.y-1)))
                p_moves.append(moves4)
        if self.y +2 <=7:
            if self.x +1 <=7:
                moves5.append(board.get_square_from_pos((self.x+1,self.y+2)))
                p_moves.append(moves5)
            if self.x-1 >=0:
                moves6.append(board.get_square_from_pos((self.x-1,self.y+2)))
                p_moves.append(moves6)
        if self.y-2>=0:
            if self.x +1 <=7:
                moves7.append(board.get_square_from_pos((self.x+1,self.y-2)))
                p_moves.append(moves7)
            if self.x-1 >=0:
                moves8.append(board.get_square_from_pos((self.x-1,self.y-2)))
                p_moves.append(moves8)

        return p_moves
    
    
