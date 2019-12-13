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
		self.direction = vec(0,0)

	# Get position of pacman and find best possible route to 4 tiles ahead of him
	def update(self):
		pass



		