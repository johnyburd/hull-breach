import pygame
tile_ids = {
    'dirt'   : pygame.image.load('res/dirt.png').convert(),
    'grass' : pygame.image.load('res/grass.png').convert(),
    'water' : pygame.image.load('res/water.png').convert(),
    'coal'  : pygame.image.load('res/coal.png').convert()
}

entity_ids = {
	'dagger'  : pygame.image.load('res/dagger.png').convert_alpha(),
	'guy'  : pygame.image.load('res/guy.png').convert_alpha()
}
