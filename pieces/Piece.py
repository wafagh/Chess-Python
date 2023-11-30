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
            for square in board.squares:
                square.highlight=False
            black_moves,white_moves,white_check_moves,black_check_moves=board.get_moves(board)
            if self.color=='white':
                if white_check_moves!= None:
                    if square in self.validate_moves(board) and  square in white_check_moves:
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                else:
                     if square in self.validate_moves(board) or force:
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True


            elif self.color=='black':
                if white_check_moves!= None:
                    if square in self.validate_moves(board) and  square in black_check_moves:
                        prev_square=board.get_square_from_pos((self.pos))
                        self.pos,self.y,self.x=square.pos,square.y,square.x
                        prev_square.piece=None
                        square.piece=self
                        board.selected_piece=None
                        self.has_moved=True
                else:
                     
                    if square in self.validate_moves(board) or force:
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
                     
            else:
                    board.selected_piece = None
                    return False






        def validate_moves(self,board):
            v_moves=[]
            white_check_moves=[]
            black_check_moves=[]
            for move in self.get_possible_moves(board):
                for square in move:
                        if self.color=='white':
                            if square.piece!=None:
                                if square.piece.color=='black':
                                    v_moves.append(move)
                                    if square.piece.notation=='K':
                                        black_check_moves.append(move)
                                else:
                                    break
                            else:
                                v_moves.append(move)
                        elif self.color=='black':
                            if square.piece!=None:
                                if square.piece.color=='white':
                                    v_moves.append(move)
                                    if square.piece.notation=='K':
                                        white_check_moves.append(move)
                                else:
                                    break
                            else:
                                v_moves.append(move)
            return v_moves,black_check_moves,white_check_moves


        