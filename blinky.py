import pygame
import collections
import math
from settings import *
from enemy_class import Enemy
from player_class import *
import pdb

vec = pygame.math.Vector2

class Blinky(Enemy):
	def __init__(self, app, pos, player_obj):
		self.color = 0xff0000
		super(Blinky, self).__init__(app, pos, player_obj, self.color)
		self.possible_directions = [[1,0],[-1,0],[0,1],[0,-1]] #right, left, up, down
		self.direction = vec(1,0)

	def update(self):
		if self.able_to_move:
			self.pix_pos += self.direction*self.speed

		#print(self.time_to_move())
		#print(int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width)

		# find next tile to move to based on possible next tiles' distance to pacman
		if self.time_to_move():
			find = self.find_next_tile(self.grid_pos, self.player.grid_pos)
			self.direction = vec(find[0],find[1])

		# Setting grid position in reference to pix position
		self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1 # grid position x-axis
		self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1 # grid position y-axis


	def find_next_tile(self, enemy_pos, player_pos):
		# get minimum linear distance from enemy to pacman for all possible tiles
		directions_allowed = [1,1,1,1] # right, left, up, down
		cursor = 0 # used to loop through directions_allowed array
		direction_to_move = 0 # holds index of directions_allowed array
		min_distance = 0

		for index, direction in enumerate(self.possible_directions):
			#print(direction[0], direction[1])
			#print(self.app.map[int(self.grid_pos.x)][int(self.grid_pos.y)])
			if self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != '1' and self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != 'B':
				distance = math.sqrt(((self.grid_pos.x+direction[0])-self.player.grid_pos.x)**2 + ((self.grid_pos.y+direction[1])-self.player.grid_pos.y)**2)
				if distance < min_distance or min_distance == 0:
					min_distance = distance
					direction_to_move = index

		print(direction_to_move)
		# return which direction to move
		if direction_to_move == 0:
			return [1,0]
		elif direction_to_move == 1:
			return [-1,0]
		elif direction_to_move == 2:
			return [0,1]
		elif direction_to_move == 3:
			return [0,-1]




