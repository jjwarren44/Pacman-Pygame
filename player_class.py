import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
	def __init__(self, app, pos):
		self.app = app
		self.grid_pos = pos
		self.pix_pos = self.get_pix_pos()
		self.direction = vec(1,0)

	def update(self):
		self.pix_pos += self.direction

		# Setting grid position in reference to pix position
		self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1 # grid position x-axis
		self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1 # grid position x-axis

	def draw(self):
		pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)

		# Draw grid position rectangle
		pygame.draw.rect(self.app.screen, WHITE, (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_BUFFER//2, 
			self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_BUFFER//2, self.app.cell_width, self.app.cell_height), 1)

	def move(self, direction):
		self.direction = direction

	def get_pix_pos(self):
		return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2, 
			(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2+self.app.cell_height//2) # so player moves by pixel, not grid (using 2d vector)







