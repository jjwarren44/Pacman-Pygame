from pygame.math import Vector2 as vec

# Screen settings
WIDTH, HEIGHT = 610, 670
TOP_BOTTOM_BUFFER = 50 # leave room for high score and lives
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER
FPS = 60

# Color settings
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (107,107,107)
PLAYER_COLOR = (190,194,15)

# Font settings
START_TEXT_SIZE = 28
START_FONT = 'arial black'

# Player settings
PLAYER_START_POS = vec(1,1)

# Mob settings