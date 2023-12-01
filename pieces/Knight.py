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
        moves=[]
        p_moves=[]
        if self.x +2 <=7:
            if self.y +1 <=7:
                moves.append(board.get_square_from_pos((self.x+2,self.y+1)))
            if self.y-1 >=0:
                moves.append(board.get_square_from_pos((self.x+2,self.y-1)))

        if self.x-2>=0:
            if self.y +1 <=7:
                moves.append(board.get_square_from_pos((self.x-2,self.y+1)))
            if self.y-1 >=0:
                moves.append(board.get_square_from_pos((self.x-2,self.y-1)))

        if self.y +2 <=7:
            if self.x +1 <=7:
                moves.append(board.get_square_from_pos((self.x+1,self.y+2)))
            if self.x-1 >=0:
                moves.append(board.get_square_from_pos((self.x-1,self.y+2)))

        if self.y-2>=0:
            if self.x +1 <=7:
                moves.append(board.get_square_from_pos((self.x+1,self.y-2)))
            if self.x-1 >=0:
                moves.append(board.get_square_from_pos((self.x-1,self.y-2)))

        for square in moves:
            if square.piece!=None:
                if square.piece.color==self.color:
                    moves.remove(square)
        p_moves.append(moves)
        #print(p_moves)
        return p_moves
    
    
