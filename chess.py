import pygame

from Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.update()


if __name__ == '__main__':
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		#print(mx,my)
		for event in pygame.event.get():
			# Quit the game if the user presses the close button
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
       			# If the mouse is clicked
				if event.button == 1:
					board.handle_click(mx, my)
		board.checkmate()
		if board.check=='white':
		#if board.is_in_checkmate('black'): # If black is in checkmate
			print('Black wins!')
			running = False
		#elif board.is_in_checkmate('white'): # If white is in checkmate
		elif board.check=='black':
			print('White wins!')
			running = False
		# Draw the board
		draw(screen)