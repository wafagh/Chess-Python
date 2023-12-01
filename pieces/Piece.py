import pygame

class Piece:

        def __init__(self, pos, color, board):
            self.pos = pos
            self.x = pos[0]
            self.y = pos[1]
            self.color = color
            self.has_moved = False
            self.board=board



        def move(self,board,square,force=False):
            for square1 in board.squares:
                square1.highlight=False
            black_moves,white_moves,white_check_moves,black_check_moves=board.get_moves(board)
            if self.color=='white':
                v_moves,b_c_moves,w_c_moves=self.validate_moves(board)
                if white_check_moves:
                    print("im here",white_check_moves)
                    if [square in v_moves] and  [square in white_check_moves]:
                        print("now im here")
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                        return True
                    else:
                        board.selected_piece = None
                        return False
                else:
                    print("ok i m here")
                    print(square)
                    print(v_moves)
                    if [square in v_moves] or force:
                        print("now im h er e")
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                        if self.notation=='K':
                            if prev_square.x - self.x==2:
                                rook=board.get_piece_from_pos((7,self.y))
                                rook.move(board,board.get_square_from_pos((3,self.y)),force=True)
                            elif prev_square.x-self.x==-2:
                                rook=board.get_piece_from_pos((7,self.y))
                                rook.move(board,board.get_square_from_pos((5,self.y)),force=True)
                        return True
                    else:
                        board.selected_piece = None
                        return False


                    


            elif self.color=='black':
                v_moves,b_c_moves,w_c_moves=self.validate_moves(board)
                if black_check_moves:

                    if [square in v_moves] and  [square in black_check_moves]:
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                        return True
                else:
                     
                    if [square in v_moves] or force:
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                        if self.notation=='K':
                            if prev_square.x - self.x==2:
                                rook=board.get_piece_from_pos((7,self.y))
                                rook.move(board,board.get_square_from_pos((3,self.y)),force=True)
                            elif prev_square.x-self.x==-2:
                                rook=board.get_piece_from_pos((7,self.y))
                                rook.move(board,board.get_square_from_pos((5,self.y)),force=True)
                
                        return True
                    else:
                        board.selected_piece = None
                        return False

                    
                     




        def validate_moves(self,board):
            v_moves=[]
            white_check_moves=[]
            black_check_moves=[]
            for move in self.get_possible_moves(board):
                #print("imhere the mvoes are",move)
                for square in move:
                        if self.color=='white':
                            if square.piece!=None:
                                if square.piece.color=='black':
                                    v_moves.append(square)
                                    if square.piece.notation=='K':
                                        black_check_moves.append(square)
                                else:
                                    break
                            else:
                                v_moves.append(square)
                        elif self.color=='black':
                            if square.piece!=None:
                                if square.piece.color=='white':
                                    v_moves.append(square)
                                    if square.piece.notation=='K':
                                        white_check_moves.append(square)
                                else:
                                    break
                            else:
                                v_moves.append(square)
            #print("this is the moves",v_moves)
            return v_moves,black_check_moves,white_check_moves


        