from pieces.Piece import Piece
import pygame


class King(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'imgs/' + color[0] + '_king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'K'

    def get_possible_moves(self,board):

        moves=[]
    
        if self.x +1 <=7 :
            moves.append(board.get_square_from_pos((self.x+1,self.y)))
        if self.x-1>=0:
            moves.append(board.get_square_from_pos((self.x-1,self.y)))
        if self.y+1<=7:
            moves.append(board.get_square_from_pos((self.x,self.y+1)))
        if self.y-1>=0:
            moves.append(board.get_square_from_pos((self.x,self.y-1)))
        if self.x+1<=7 and self.y+1<=7:
            moves.append(board.get_square_from_pos((self.x+1,self.y+1)))
        if self.x+1<=7 and self.y-1>=0:
            moves.append(board.get_square_from_pos((self.x+1,self.y-1)))
        if self.x-1>=0 and self.y+1<=7:
            moves.append(board.get_square_from_pos((self.x-1,self.y+1)))
        if self.x-1>=0 and self.y-1>=0:
            moves.append(board.get_square_from_pos((self.x-1,self.y-1)))
        
        if self.has_moved ==False:
            if self.color=='white':
                kingside_rook=board.get_piece_from_pos((7,7))
                queenside_rook=board.get_piece_from_pos((0,7))

                if kingside_rook!=None:
                    if kingside_rook.has_moved==False:
                        if board.get_piece_from_pos((6,7))==None and board.get_piece_from_pos((5,7))==None:
                            moves.append(board.get_square_from_pos((6,7)))
                if queenside_rook!=None:
                    if queenside_rook.has_moved==False:
                        if [board.get_piece_from_pos((i,7))for i in range(1,4)]==[None,None,None]:
                            moves.append(board.get_square_from_pos((2,7)))

            elif self.color=='black':
                kingside_rook=board.get_piece_from_pos((7,0))
                queenside_rook=board.get_piece_from_pos((0,0))

                if kingside_rook!=None:
                    if kingside_rook.has_moved==False:
                        if board.get_piece_from_pos((6,0))==None and board.get_piece_from_pos((5,0))==None:
                            moves.append(board.get_square_from_pos((6,0)))
                if queenside_rook!=None:
                    if queenside_rook.has_moved==False:
                        if [board.get_piece_from_pos((i,0))for i in range(1,4)]==[None,None,None]:
                            moves.append(board.get_square_from_pos((2,0)))
        
        return moves
    
    

                


