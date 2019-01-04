import pygame, sys, random
from game import Game
from gamemap import Map
from pygame.locals import *
pygame.font.init()
clock = pygame.time.Clock()

myfont = pygame.font.SysFont('Comic Sans MS', 40)

message_log = "hello\nthis is a message\nthis is cool"

TILESIZE  = 30
MAPWIDTH  = 50
MAPHEIGHT = 30

game = Game(MAPWIDTH, MAPHEIGHT)

pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE), pygame.RESIZABLE)
old_map = [[None for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]

from tile_ids import tile_ids, entity_ids
scaled_tile_ids = {}
scaled_entity_ids = {}
for k, i in tile_ids.items():
    scaled_tile_ids[k] = pygame.transform.scale(i, (int(TILESIZE), int(TILESIZE)))
for k, i in entity_ids.items():
    scaled_entity_ids[k] = pygame.transform.scale(i, (int(TILESIZE), int(TILESIZE)))

while True:
    clock.tick(30)
    #print(screen.get_width()) # 1500
    #print(screen.get_height()) # 900
    dirty_tiles = []

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            print(event.size)
            old_screen = screen
            #MAPWIDTH = int(event.w / 30)
            #MAPHEIGHT = int(event.h / 30)
            TILESIZE = min(event.w / MAPWIDTH, event.h / MAPHEIGHT)
            print(TILESIZE)
            for k, i in tile_ids.items():
                scaled_tile_ids[k] = pygame.transform.scale(i, (int(TILESIZE), int(TILESIZE)))
            for k, i in entity_ids.items():
                scaled_entity_ids[k] = pygame.transform.scale(i, (int(TILESIZE), int(TILESIZE)))
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
            dirty_tiles.append(pygame.Rect(0,0, event.w, event.h))
            old_map = [[None for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]

    tilemap = game.current_level.array
    entitymap = game.current_level.entitylist

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            if tilemap[row][column] != old_map[row][column]:
                dirty_tiles.append(pygame.Rect(column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
                screen.blit(scaled_tile_ids[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
            if entitymap[row][column]:
                screen.blit(scaled_entity_ids[entitymap[row][column]], (column*TILESIZE,row*TILESIZE))
                dirty_tiles.append(pygame.Rect(column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            count = 0
            for line in message_log.split('\n'):
                textsurface = myfont.render(line, False, (0, 0, 0))
                screen.blit(textsurface,(0,count))
                count += 40
    old_map = tilemap

    #update the display
    #print(dirty_tiles)
    pygame.display.update(dirty_tiles)
    #time.sleep(30.0 - ((time.time() - starttime) % 30.0))
