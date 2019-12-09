import pygame
from settings import *
from enemy_class import Enemy

vec = pygame.math.Vector2

class Inky(Enemy):
	def __init__(self, app, pos, player_obj):
		self.color = 0x00ffff
		super(Inky, self).__init__(app, pos, player_obj, self.color)


		