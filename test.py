import pygame, sys, random
from tile_ids import tile_ids
from game import Game
import time
from gamemap import Map
from pygame.locals import *
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

message_log = "hello\nthis is a message\nthis is cool"

TILESIZE  = 30
MAPWIDTH  = 50
MAPHEIGHT = 40

game = Game(MAPWIDTH, MAPHEIGHT)

pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
starttime=time.time()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    tilemap = game.current_level().array

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            screen.blit(tile_ids[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
            count = 0
            for line in message_log.split('\n'):
                textsurface = myfont.render(line, False, (0, 0, 0))
                screen.blit(textsurface,(0,count))
                count += 40

    #update the display
    pygame.display.update()
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))
