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
        moves1,moves2,moves3,moves4,moves5,moves6,moves7,moves8,moves9,moves10=[],[],[],[],[],[],[],[],[],[]
        p_moves=[]
        if self.x +1 <=7 :
            moves1.append(board.get_square_from_pos((self.x+1,self.y)))
            p_moves.append(moves1)
        if self.x-1>=0:
            moves2.append(board.get_square_from_pos((self.x-1,self.y)))
            p_moves.append(moves2)
        if self.y+1<=7:
            moves3.append(board.get_square_from_pos((self.x,self.y+1)))
            p_moves.append(moves3)
        if self.y-1>=0:
            moves4.append(board.get_square_from_pos((self.x,self.y-1)))
            p_moves.append(moves4)
        if self.x+1<=7 and self.y+1<=7:
            moves5.append(board.get_square_from_pos((self.x+1,self.y+1)))
            p_moves.append(moves5)
        if self.x+1<=7 and self.y-1>=0:
            moves6.append(board.get_square_from_pos((self.x+1,self.y-1)))
            p_moves.append(moves6)
        if self.x-1>=0 and self.y+1<=7:
            moves7.append(board.get_square_from_pos((self.x-1,self.y+1)))
            p_moves.append(moves7)
        if self.x-1>=0 and self.y-1>=0:
            moves8.append(board.get_square_from_pos((self.x-1,self.y-1)))
            p_moves.append(moves8)
        
        for square in board.squares:
                if square.piece!=None:
                    square.piece.guarded=False
        black_moves,white_moves,white_check_squares,black_check_squares=board.get_moves(board)
        
        if self.has_moved ==False:
            
            if self.color=='white':
                kingside_rook=board.get_piece_from_pos((7,7))
                queenside_rook=board.get_piece_from_pos((0,7))
                if self.check_move(black_moves,board,4,7,7):
                    if kingside_rook!=None:
                        if kingside_rook.has_moved==False:
                            if board.get_piece_from_pos((6,7))==None and board.get_piece_from_pos((5,7))==None:
                                moves9.append(board.get_square_from_pos((6,7)))
                                p_moves.append(moves9)
                if self.check_move(black_moves,board,2,5,7):
                    if queenside_rook!=None:
                        if queenside_rook.has_moved==False:
                            if [board.get_piece_from_pos((i,7))for i in range(1,4)]==[None,None,None]:
                                moves10.append(board.get_square_from_pos((2,7)))
                                p_moves.append(moves10)
                
            elif self.color=='black':
                kingside_rook=board.get_piece_from_pos((7,0))
                queenside_rook=board.get_piece_from_pos((0,0))
                if self.check_move(white_moves,board,4,7,0):
                    if kingside_rook!=None:
                        if kingside_rook.has_moved==False:
                            if board.get_piece_from_pos((6,0))==None and board.get_piece_from_pos((5,0))==None:
                                moves9.append(board.get_square_from_pos((6,0)))
                                p_moves.append(moves9)
                if self.check_move(white_moves,board,2,5,0):                
                    if queenside_rook!=None:
                        if queenside_rook.has_moved==False:
                            if [board.get_piece_from_pos((i,0))for i in range(1,4)]==[None,None,None]:
                                moves10.append(board.get_square_from_pos((2,0)))
                                p_moves.append(moves10)
        
        if self.color=='white':
            p_moves=self.possible_moves(p_moves,black_moves)
        else:
            p_moves=self.possible_moves(p_moves,white_moves)
        
        return p_moves
    
    def possible_moves(self,moves,attacked_moves):
        flat_moves = [item for sublist in moves for item in sublist]
        pos_moves=[]
        impos_moves=[]
        for move in attacked_moves:
            for square in flat_moves:
                if square==move:
                    impos_moves.append(square)
        for move in flat_moves:
            if move not in impos_moves:
                if move.piece!=None:
                    if move.piece.color!=self.color:
                        if move.piece.guarded==False:
                            pos_moves.append(move)
                else:
                    pos_moves.append(move)
        
        return [[el] for el in pos_moves]
                

    def check_move(self,moves,board,i,j,y):
        if len(moves)==0:
            return True
        else:
            for square in moves:
                for z in range(i,j):
                    if board.get_square_from_pos((z,y))==square:
                        return False
            return True