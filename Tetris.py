"""
The following is a work in progress to clone the
game "Tetris". The ownership of the game goes to
Henk Rogers and Alexey Pajitnov and I claim no
ownership of the game.
"""

import pygame
import random
pygame.init()

# size of window and setting it up
display_width = 550
display_height = 550
gameDisplay = pygame.display.set_mode((display_width, display_height))

# frame tick
clock = pygame.time.Clock()

# font
largefont = pygame.font.SysFont("timesnewroman", 135)

# words on screen
word = [largefont.render('PAUSE', False,(255,255,255))]

# images for the game
backgroundImage = pygame.image.load("TetrisBoard.png")
squares = pygame.image.load("Squares.png")

# music
pygame.mixer.music.load('TetrisTheme.mp3')
pygame.mixer.music.play(-1)

### One Block ###
def base(x,y,squareList):
    # draws the one block
    gameDisplay.blit(squares,(x,y),(0,0,25,25))
    
    # if the block hits the ground or hits the top of another block, return the squareList
    if y == 525 or gameDisplay.get_at((x+12, y+36))!=((1,1,1,255)):
        squareList.append((x,y,0))
        return squareList
    # otherwise, return 1
    else:
        return 1
    
### Long Block ###
def longBlock(x,y,squareList,rotation):
    # draws all 4 blocks
    gameDisplay.blit(squares,(x,y),(75,0,25,25))
    gameDisplay.blit(squares,(x,y+25),(75,0,25,25))
    gameDisplay.blit(squares,(x,y+50),(75,0,25,25))
    gameDisplay.blit(squares,(x,y+75),(75,0,25,25))

    # if the block hits the ground or hits the top of another block, return the squareList
    if y == 450 or gameDisplay.get_at((x+12, y+112))!=((1,1,1,255)):
        squareList.append((x,y,3))
        squareList.append((x,y+25,3))
        squareList.append((x,y+50,3))
        squareList.append((x,y+75,3))
        return squareList
    # otherwise, return 1
    else:
        return 1

### Game Method ###
def gameLoop():
    # sets base value
    gameExit = pause = False
    squareOnScreen = 1

    # x value and y value of block
    xVal = 275
    y = 0
    
    # rotation of block
    rotation = 0

    # list for all the blocks on screen
    squareList = []

    ### Game Starts ###
    while not gameExit:
        for event in pygame.event.get():
            # if exit is pressed on window, exit the window
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                # moves the block left and right as long as the game isn't paused
                if event.key == pygame.K_LEFT:
                    if gameDisplay.get_at((xVal-12, y+12))==((1,1,1,255)) and not pause:
                        xVal-=25
                elif event.key == pygame.K_RIGHT:
                    if gameDisplay.get_at((xVal+36, y+36))==((1,1,1,255)) and not pause:
                        xVal+=25

                # space pauses and unpauses the game
                elif event.key == pygame.K_SPACE:
                    if not pause:
                        pause = True
                    else:
                        pause = False

        # fill screen with white
        gameDisplay.fill((255,255,255))
        # background image is placed on screen
        gameDisplay.blit(backgroundImage,(0,0),(0,0,550,550))

        # if the squareList isn't empty, draw squares on screen
        if len(squareList) != 0:
            for x in squareList:
                gameDisplay.blit(squares,(int(x[0]),int(x[1])),(25*int(x[2]),0,25,25))

        # if the game is paused, draw the word "PAUSED" on screen
        if pause == True:
            gameDisplay.blit(word[0],(91,187))
        # otherwise, bring the blocks down
        else:
            # updates block position
            squareOnScreen = longBlock(xVal,y,squareList,rotation)

            # if squareOnScreen does not return 1, and instead returns a list
            if not squareOnScreen == 1:
                # update the list
                squareList = squareOnScreen
                
                # renew the values
                xVal = 275
                y = 0
            # bring the block down 
            y += 25

        # update the screen and tick for 5 frames
        pygame.display.update()
        clock.tick(5)

    ### End The Game Start ###

    # closes the game window
    pygame.quit()

### End of the Game Method ###





# calls the gameLoop method
gameLoop()



    

