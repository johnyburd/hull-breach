import pygame, sys, random
from game import Game
from gamemap import Map
from pygame.locals import *
pygame.font.init()
clock = pygame.time.Clock()

myfont = pygame.font.SysFont('Comic Sans MS', 40)

message_log = ["hello","this is a message","this is cool"]

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
    scaled_tile_ids[k] = pygame.transform.scale(i, (TILESIZE, TILESIZE))
for k, i in entity_ids.items():
    scaled_entity_ids[k] = pygame.transform.scale(i, (TILESIZE, TILESIZE))

while True:
    clock.tick(30)
    dirty_tiles = []

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                game.move_player('w')
            elif event.key == pygame.K_RIGHT:
                game.move_player('e')
            elif event.key == pygame.K_DOWN:
                game.move_player('s')
            elif event.key == pygame.K_UP:
                game.move_player('n')
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            print(event.size)
            old_screen = screen
            TILESIZE = int(min(event.w / MAPWIDTH, event.h / MAPHEIGHT))
            print(int(TILESIZE))
            for k, i in tile_ids.items():
                scaled_tile_ids[k] = pygame.transform.scale(i, (TILESIZE, TILESIZE))
            for k, i in entity_ids.items():
                scaled_entity_ids[k] = pygame.transform.scale(i, (TILESIZE, TILESIZE))
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
            dirty_tiles.append(pygame.Rect(0,0, event.w, event.h))
            old_map = [[None for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]

    tilemap = game.current_level.array
    entitymap = game.current_level.entitylist

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            if tilemap[row][column] != old_map[row][column]:
                dirty_tiles.append(pygame.Rect(column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
                screen.blit(scaled_tile_ids[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
            if entitymap[row][column]:
                screen.blit(scaled_entity_ids[entitymap[row][column]], (column*TILESIZE,row*TILESIZE))
                dirty_tiles.append(pygame.Rect(column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            count = 0
            for line in message_log:
                textsurface = myfont.render(line, False, (0, 0, 0))
                screen.blit(textsurface,(0,count))
                count += 40
    old_map = tilemap

    pygame.display.update(dirty_tiles)
