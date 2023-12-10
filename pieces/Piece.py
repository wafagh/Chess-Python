import pygame

class Piece:

        def __init__(self, pos, color, board):
            self.pos = pos
            self.x = pos[0]
            self.y = pos[1]
            self.color = color
            self.has_moved = False
            self.board=board
            self.guarded=False
            self.pin=False

        def move(self,board,square,force=False):
            check=False
            output=[]
            check,output=board.king_in_check(self)
            print(output)
            for square1 in board.squares:
                square1.highlight=False
            if check or force:
                #print("white in check here",white_check_moves)
                if square in output or force:
                    print("square",square)
                    print(output)
                    prev_square=board.get_square_from_pos((self.pos))
                    self.pos,self.y,self.x=square.pos,square.y,square.x
                    prev_square.piece=None
                    square.piece=self
                    board.selected_piece=None
                    self.has_moved=True
                    if self.notation=='K':
                        if prev_square.x - self.x==2:
                            rook=board.get_piece_from_pos((0,self.y))
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
            temp_move=[]
                  
            for move in self.get_possible_moves(board):
                for square in move:
                        if self.color=='white':
                            if square.piece!=None:
                                if square.piece.color=='black':
                                    v_moves.append(square)
                                    if square.piece.notation=='K':
                                        temp_move=move
                                        temp_move.extend([board.get_square_from_pos(self.pos)])
                                        black_check_moves.append(temp_move)
                                        break
                                    else:
                                        index=move.index(square)
                                        if move[index+1]!=None:
                                            if move[index+1].piece.color=='black'and move[index+1].piece.notation=='K':
                                                square.piece.pin=True
                                        break
                                else:
                                    square.piece.guarded=True
                                    break
                            else:
                                v_moves.append(square)
                        elif self.color=='black':
                            if square.piece!=None:
                                if square.piece.color=='white':
                                    v_moves.append(square)
                                    if square.piece.notation=='K':
                                        temp_move=move
                                        temp_move.extend([board.get_square_from_pos(self.pos)])
                                        white_check_moves.append(temp_move)
                                        break
                                    else:
                                        index=move.index(square)
                                        if move[index+1]!=None:
                                            if move[index+1].piece.color=='white'and move[index+1].piece.notation=='K':
                                                square.piece.pin=True
                                        break
                                else:
                                    square.piece.guarded=True
                                    break
                            else:
                                v_moves.append(square)
            return v_moves,black_check_moves,white_check_moves


        