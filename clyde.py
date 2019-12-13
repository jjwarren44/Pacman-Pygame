import pygame
from settings import *
from enemy_class import Enemy

vec = pygame.math.Vector2

class Clyde(Enemy):
	def __init__(self, app, pos, player_obj):
		self.color = 0xffa500
		super(Clyde, self).__init__(app, pos, player_obj, self.color)

	# Get position of pacman and find best possible route to 4 tiles ahead of him
	def update(self):
		pass