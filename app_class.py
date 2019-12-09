import pygame, sys
from settings import * # custom settings file
from player_class import *

pygame.init()
vec = pygame.math.Vector2

class App:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.state = 'start' # start at start screen
		self.cell_width = MAZE_WIDTH//28 # init grid
		self.cell_height = MAZE_HEIGHT//30 # init grid
		self.player = Player(self, PLAYER_START_POS) # init player
		self.walls = []
		self.coins = []

		self.load()

	def run(self):
		while self.running:
			if self.state == 'start':
				self.start_events()
				self.start_update()
				self.start_draw()
			elif self.state == 'playing':
				self.playing_events()
				self.playing_update()
				self.playing_draw()				
			self.clock.tick(FPS) # 60, FPS in settings file
		pygame.quit()
		sys.exit()

######################## HELPER FUNCTIONS ##############################

	def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
		font = pygame.font.SysFont(font_name, size)
		text = font.render(words, False, color)
		text_size = text.get_size()
		if centered:
			pos[0] = pos[0] - text_size[0] // 2
			pos[1] = pos[1] - text_size[1] // 2
		screen.blit(text, pos)

	# Load images and walls on init
	def load(self):
		self.background = pygame.image.load('imgs/background.png')
		self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT)) # Scale background to window size
		with open('walls.txt', 'r') as file: # read in walls file and create walls list for wall coordinates
			for yindex, line in enumerate(file): # enumerate to get coordinates
				for xindex, char in enumerate(line):
					if char == '1': # if wall,  set coordinate to boundary
						self.walls.append(vec(xindex, yindex))
					elif char == 'C': # if coin, set coordinate to coin
						self.coins.append(vec(xindex, yindex))

	'''
	# draw grid for movement
	def draw_grid(self):
		for x in range(WIDTH//self.cell_width):
			pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
		for x in range(HEIGHT//self.cell_height):
			pygame.draw.line(self.background, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))
		for coin in self.coins: # draw coins
			pygame.draw.rect(self.background, (167,179,34), 
				(coin.x*self.cell_width, coin.y*self.cell_height, self.cell_width, self.cell_height))
	'''

######################## INTRO FUNCTIONS ##############################

	def start_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.state = 'playing'

	def start_update(self):
		pass

	def start_draw(self):
		self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2 - 50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True) # PUSH SPACE BAR text
		self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2 + 50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True) # 1 PLAYER ONLY text
		self.draw_text('HIGH SCORE', self.screen, [4,0], START_TEXT_SIZE, WHITE, START_FONT) # HIGH SCORE text
		pygame.display.update()


######################## PLAYING FUNCTIONS ##############################

	def playing_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.move(vec(-1,0))
				if event.key == pygame.K_RIGHT:
					self.player.move(vec(1,0))
				if event.key == pygame.K_UP:
					self.player.move(vec(0,-1))
				if event.key == pygame.K_DOWN:
					self.player.move(vec(0,1))

	def playing_update(self):
		self.player.update()

	def playing_draw(self):
		self.screen.fill(BLACK)
		self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
		self.draw_coins()
		# self.draw_grid()
		self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score), self.screen, [60, 2], START_TEXT_SIZE, WHITE, START_FONT)
		self.draw_text('HIGH SCORE: 0', self.screen, [WIDTH//2+60, 2], START_TEXT_SIZE, WHITE, START_FONT)
		self.player.draw() # draw player
		pygame.display.update()
		# self.coins.pop()

	def draw_coins(self):
		for coin in self.coins:
			pygame.draw.circle(self.screen, (124,123,7), 
				((int(coin.x*self.cell_width)+self.cell_width//2)+TOP_BOTTOM_BUFFER//2, 
					(int(coin.y*self.cell_height)+self.cell_height//2)+TOP_BOTTOM_BUFFER//2), 3)



