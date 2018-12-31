import pygame, sys, random
from pygame.locals import *
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

message_log = "hello\nthis is a message\nthis is cool"

#constants representing the different resources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3

#a dictionary linking resources to textures
textures =   {
                DIRT   : pygame.image.load('res/dirt.png'),
                GRASS : pygame.image.load('res/grass.png'),
                WATER : pygame.image.load('res/water.png'),
                COAL  : pygame.image.load('res/coal.png')
            }

#useful game dimensions
TILESIZE  = 40
MAPWIDTH  = 50
MAPHEIGHT = 40

#a list of resources
resources = [DIRT,GRASS,WATER,COAL]
#use list comprehension to create our tilemap
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

#set up the display
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#loop through each row
for rw in range(MAPHEIGHT):
    #loop through each column in that row
    for cl in range(MAPWIDTH):
        #pick a random number between 0 and 15
        randomNumber = random.randint(0,15)
        #if a zero, then the tile is coal
        if randomNumber == 0:
            tile = COAL
        #water if the random number is a 1 or a 2
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        #set the position in the tilemap to the randomly chosen tile
        tilemap[rw][cl] = tile

while True:

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()

    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            screen.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
            count = 0
            for line in message_log.split('\n'):
                textsurface = myfont.render(line, False, (0, 0, 0))
                screen.blit(textsurface,(0,count))
                count += 40



    #update the display
    pygame.display.update()
