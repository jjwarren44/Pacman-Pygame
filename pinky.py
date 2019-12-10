import pygame
import collections
from settings import *
from enemy_class import Enemy
from player_class import *

vec = pygame.math.Vector2

class Pinky(Enemy):
	def __init__(self, app, pos, player_obj):
		self.color = 0xffc0cb
		self.shortest_path = []
		super(Pinky, self).__init__(app, pos, player_obj, self.color)
		self.direction = vec(1,0)

	# Get position of pacman and find best possible route to 4 tiles ahead of him
	def update(self):
		self.shortest_path = self.find_shortest_path(self.grid_pos, self.player.get_grid_pos())
		if self.shortest_path != None:
			for (x, y) in self.shortest_path:
				pygame.draw.rect(self.app.background, GREY, (x*self.app.cell_width, 
				y*self.app.cell_height, self.app.cell_width, self.app.cell_height))

		# find which direction to go 
		if self.shortest_path != None and len(self.shortest_path) > 4:
			if self.shortest_path[1][0] > self.grid_pos.x: # if next cell on path is to the right
				self.stored_direction = vec(1,0)
			elif self.shortest_path[1][0] < self.grid_pos.x: # if next cell on path is to the left
				self.stored_direction = vec(-1,0)
			elif self.shortest_path[1][1] > self.grid_pos.y: # if next cell on path is up
				self.stored_direction = vec(0,1)
			else: # if next cell on path is down
				self.stored_direction = vec(0,-1)

		# move enemy's position
		# Keep player on the grid, can't be on a line but has to be within the lines
		if self.able_to_move:
			self.pix_pos += self.direction*self.speed

		# Keep player on the grid, can't be on a line but has to be within the lines
		if self.time_to_move():
			if self.stored_direction != None:
				self.direction = self.stored_direction
			self.able_to_move = self.can_move()

		# Setting grid position in reference to pix position
		self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1 # grid position x-axis
		self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1 # grid position x-axis
			

	# breadth first search, find shortest path to 4 tiles in front of player
	def find_shortest_path(self, enemy_pos, player_pos):
		# draw over old path
		if self.shortest_path != None:
			for (x, y) in self.shortest_path:
				pygame.draw.rect(self.app.background, BLACK, (x*self.app.cell_width, 
				y*self.app.cell_height, self.app.cell_width, self.app.cell_height))

		queue = collections.deque([[(int(enemy_pos.x), int(enemy_pos.y))]])
		seen = set([int(enemy_pos.x), int(enemy_pos.y)])
		width = len(self.app.map[0])
		height = len(self.app.map)
		while queue:
			path = queue.popleft()
			x, y = path[-1]
			# check to see what direction pacman is facing, send ghost torward 4 tiles in front of stored.direction
			if self.player.direction == vec(1,0): # moving right
				if int(x) == player_pos.x+4 and int(y) == player_pos.y:
					return path
			elif self.player.direction == vec(-1,0): # moving left
				if int(x) == player_pos.x-4 and int(y) == player_pos.y:
					return path
			elif self.player.direction == vec(0,1): # moving up
				if int(x) == player_pos.x and int(y) == player_pos.y+4:
					return path
			elif self.player.direction == vec(0,-1): # moving down
				if int(x) == player_pos.x and int(y) == player_pos.y-4:
					return path

			for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
				if 0 <= x2 < width and 0 <= y2 < height and self.app.map[y2][x2] != '1' and (x2, y2) not in seen:
					queue.append(path + [(x2, y2)])
					seen.add((x2, y2))



		