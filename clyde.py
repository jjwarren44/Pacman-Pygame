import pygame
import collections
import math
from settings import *
from enemy_class import Enemy
from player_class import *
import pdb

vec = pygame.math.Vector2

class Clyde(Enemy):
	def __init__(self, app, pos, player_obj):
		self.color = 0xffa500
		self.img = pygame.image.load("imgs/clyde.png")
		super(Clyde, self).__init__(app, pos, player_obj, self.img)
		self.possible_directions = [[1,0],[-1,0],[0,1],[0,-1]] #right, left, down, up
		self.direction = vec(0,0)
		self.in_ghost_house = True

	def update(self):
		if pygame.time.get_ticks() - self.app.game_start_time > 9000:

			self.pix_pos += self.direction*self.speed # move

			if self.in_ghost_house: # manually move left 2 and up 2
				if self.grid_pos.x == 16 and self.grid_pos.y == 15:
					self.direction = vec(-1,0)
				if self.grid_pos.x == 14 and self.grid_pos.y == 15:
					self.direction = vec(0,-1)
				if self.grid_pos.x == 14 and self.grid_pos.y == 11:
					self.in_ghost_house = False
			else:
				if self.time_to_move():
					if abs(self.grid_pos.x-self.player.grid_pos.x) > 8 or abs(self.grid_pos.y-self.player.grid_pos.y) > 8:
						find = self.chase_find_next_tile(self.player.grid_pos)
						self.direction = vec(find[0],find[1])
					else:
						find = self.scatter_find_next_tile()
						self.direction = vec(find[0],find[1])

		# Setting grid position in reference to pix position
		self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1 # grid position x-axis
		self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1 # grid position y-axis

	def chase_find_next_tile(self, player_pos):
		# get minimum linear distance from enemy to pacman for all possible tiles
		direction_to_move = 0 # holds index of directions_allowed array
		min_distance = 0

		# Loop through possible directions to check if there is a wall or ghost house gate on that tile. Also, ghosts can't turn around
		# If there isn't, find linear path to pacman
		# return minimum from all of these possible tiles
		for index, direction in enumerate(self.possible_directions):
			if direction != self.direction*-1 and self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != '1' and self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != 'G':
				distance = math.sqrt(((self.grid_pos.x+direction[0])-player_pos.x)**2 + ((self.grid_pos.y+direction[1])-player_pos.y)**2)
				if distance < min_distance or min_distance == 0:
					min_distance = distance
					direction_to_move = index

		# return which direction to move
		if direction_to_move == 0:
			return [1,0]
		elif direction_to_move == 1:
			return [-1,0]
		elif direction_to_move == 2:
			return [0,1]
		elif direction_to_move == 3:
			return [0,-1]

	def scatter_find_next_tile(self):
		# get minimum linear distance from enemy to pacman for all possible tiles
		direction_to_move = 0 # holds index of directions_allowed array
		min_distance = 0

		target_tile = vec(1,30)

		# Loop through possible directions to check if there is a wall or ghost house gate on that tile. Also, ghosts can't turn around
		# If there isn't, find linear path to home corner (bottom left)
		# return minimum from all of these possible tiles
		for index, direction in enumerate(self.possible_directions):
			if direction != self.direction*-1 and self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != '1' and self.app.map[int(self.grid_pos.y+direction[1])][int(self.grid_pos.x+direction[0])] != 'G':
				distance = math.sqrt(((self.grid_pos.x+direction[0])-target_tile.x)**2 + ((self.grid_pos.y+direction[1])-target_tile.y)**2)
				if distance < min_distance or min_distance == 0:
					min_distance = distance
					direction_to_move = index

		# return which direction to move
		if direction_to_move == 0:
			return [1,0]
		elif direction_to_move == 1:
			return [-1,0]
		elif direction_to_move == 2:
			return [0,1]
		elif direction_to_move == 3:
			return [0,-1]