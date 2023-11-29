from pieces.Piece import Piece
import pygame


class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'imgs/' + color[0] + '_queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'Q'


    def get_possible_moves(self,board):
        moves=[]
        moves_n=[]
        for i in range(1,8):
            if self.x +i >7 :
                break
            moves_n.append(board.get_square_from_pos((self.x+i,self.y)))
            
        
        moves.append(moves_n)
        
        moves_s=[]
        for i in range(1,8):
            if self.x -i <0 :
                break
            moves_s.append(board.get_square_from_pos((self.x-i,self.y)))
            
        
        moves.append(moves_s)

        moves_e=[]
        for i in range(1,8):
            if self.y +i >7 :
                break
            moves_e.append(board.get_square_from_pos((self.x,self.y+i)))
        
        moves.append(moves_e)

        moves_w=[]
        for i in range(1,8):
            if self.y -i <0 :
                break
            moves_w.append(board.get_square_from_pos((self.x,self.y-i)))
            
        
        moves.append(moves_w)
        
        
        moves_n_e=[]
        for i in range(1,8):
            if self.x +i >7 or self.y+i>7 :
                break
            moves_n_e.append(board.get_square_from_pos((self.x+i,self.y+i)))
            
        moves.append(moves_n_e)

        moves_n_w=[]
        for i in range(1,8):
            if self.x +i >7 or self.y-i< 0:
                break
            moves_s_w.append(board.get_square_from_pos((self.x+i,self.y)))
        moves.append(moves_n_w)


        moves_s_w=[]
        for i in range(1,8):
            if self.x -i <0 or self.y-i< 0:
                break
            moves_s_w.append(board.get_square_from_pos((self.x+i,self.y)))
        moves.append(moves_s_w)

        moves_s_e=[]
        for i in range(1,8):
            if self.x -i <0 or self.y+i> 7:
                break
            moves_s_e.append(board.get_square_from_pos((self.x+i,self.y)))
        moves.append(moves_s_e)
    
        return moves