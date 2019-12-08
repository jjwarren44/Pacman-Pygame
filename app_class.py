import pygame, sys
from settings import * # custom settings file

pygame.init()
vec = pygame.math.Vector2

class App:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.state = 'start'
		self.cell_width = WIDTH//28
		self.cell_height = HEIGHT//30

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

	# Load images on init
	def load(self):
		self.background = pygame.image.load('imgs/background.png')
		self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT)) # Scale background to window size

	# draw grid for movement
	def draw_grid(self):
		for x in range(WIDTH//self.cell_width):
			pygame.draw.line(self.screen, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
		for x in range(HEIGHT//self.cell_height):
			pygame.draw.line(self.screen, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))

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

	def playing_update(self):
		pass

	def playing_draw(self):
		self.screen.blit(self.background, (0,0))
		self.draw_grid()
		pygame.display.update()