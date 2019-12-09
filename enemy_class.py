import pygame
from settings import *

vec = pygame.math.Vector2

class Enemy(object):
	def __init__(self, app, pos, player_obj, color):
		self.app = app
		self.grid_pos = pos
		self.pix_pos = self.get_pix_pos()
		self.direction = vec(0,0)
		self.stored_direction = None
		self.color = color
		self.speed = 1
		self.able_to_move = True
		self.player = player_obj

	def update(self):
		self.pix_pos += self.direction
		if self.time_to_move():
			self.move()

		# Setting grid position in reference to pix position
		self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1 # grid position x-axis
		self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1 # grid position x-axis

	def draw(self):
		pygame.draw.circle(self.app.screen, self.color, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)

	def time_to_move(self):
		if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
			if self.direction == vec(1,0) or self.direction == vec(-1, 0):
				return True

		if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:					
			if self.direction == vec(0,1) or self.direction == vec(0,-1):
				return True

		# else
		return False

	# Function to handle whether or not there is a wall in the way
	def can_move(self):
		for wall in self.app.walls:
			if vec(self.grid_pos+self.direction) == wall: # if player hits wall, dont allow movement
				return False
		return True

	def move(self):
		self.stored_direction = self.direction

	def get_pix_pos(self):
		return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2, 
			(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2+self.app.cell_height//2) # so enemy moves by pixel, not grid (using 2d vector)

		