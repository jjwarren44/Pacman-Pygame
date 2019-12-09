import pygame
from settings import *

vec = pygame.math.Vector2

class Enemy:
	def __init__(self, app, pos, number):
		self.app = app
		self.grid_pos = pos
		self.pix_pos = self.get_pix_pos()
		self.radius = int(self.app.cell_width//2.3)
		self.number = number
		self.color = self.set_color()
		self.direction = vec(0,0)
		self.personality = self.set_personality()

	def update(self):
		self.pix_pos += self.direction
		if self.time_to_move:
			self.move()

	def draw(self):
		pygame.draw.circle(self.app.screen, self.color, (int(self.pix_pos.x), int(self.pix_pos.y)), self.radius)

	def time_to_move(self):
		if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
			if self.direction == vec(1,0) or self.direction == vec(-1, 0):
				return True

		if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:					
			if self.direction == vec(0,1) or self.direction == vec(0,-1):
				return True

		# else
		return False

	def move(self):
		pass

	def get_pix_pos(self):
		return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2, 
			(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2+self.app.cell_height//2) # so enemy moves by pixel, not grid (using 2d vector)

	def set_color(self):
		if self.number == 0:
			return (43,78,203)
		if self.number == 1:
			return (197,200,27)
		if self.number == 2:
			return (189,29,29)
		if self.number == 3:
			return (215,159,33)

	def set_personality(self):
		if self.number == 0:
			return "blinky"
		elif self.number == 1:
			return "pinky"		
		elif self.number == 2:
			return "inky"
		else
			return "clyde"			