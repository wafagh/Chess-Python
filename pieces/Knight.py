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

        return moves
    
    def validate_moves(self,board):
        v_moves=[]
        for move in self.get_possible_moves(board):
            if self.color=='white':
                if move.piece!=None:
                    if move.piece.color=='black':
                        v_moves.append(move)
                else:
                    v_moves.append(move)
            elif self.color=='black':
                if move.piece!=None:
                    if move.piece.color=='white':
                        v_moves.append(move)
                else:
                    v_moves.append(move)
