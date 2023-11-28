from pieces.Piece import Piece
import pygame


class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)

        img_path = 'imgs/' + color[0] + '_knight.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'N'