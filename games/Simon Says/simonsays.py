# Simple Simon Says
# By Max Kern kernmx@mail.uc.edu

import random, sys, time, pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
XMARGIN = WIDTH // 10
YMARGIN = HEIGHT // 10
DELAY = 2000 # in milliseconds
SHORTDELAY = 1000 # in millisecond

WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
YELLOW = pygame.Color('yellow')
BGCOLOR = pygame.Color('gray')

RECT = pygame.Rect(XMARGIN, YMARGIN, WIDTH - (2*XMARGIN), HEIGHT - (2*YMARGIN))

def main():
    global clock, correct, wrong, screen

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Simon Says')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    correct = pygame.mixer.Sound('right.wav')
    wrong = pygame.mixer.Sound('wrong.wav')

    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    step = 0 # the color the player must push next
    actionTime = 0 # timestamp of the player's last button push
    level = 1
    userInput = False

    while True: # main game loop
        screen.fill(BGCOLOR)
        pygame.draw.rect(screen, BGCOLOR, RECT)
        pygame.display.flip()
        selected = None

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == KEYDOWN:
                if event.key == K_y:
                    selected = YELLOW
                elif event.key == K_b:
                    selected = BLUE
                elif event.key == K_r:
                    selected = RED
                elif event.key == K_g:
                    selected = GREEN

        if not userInput: # Show the player the pattern
            pygame.display.update()
            pygame.time.wait(DELAY)
            pattern.clear() #Remove the previous pattern

            # Add new colors, as many colors as the current level
            for i in range(level):
                pattern.append(random.choice([YELLOW, BLUE, RED, GREEN]))

            # Display the pattern
            for color in pattern:
                pygame.draw.rect(screen, color, RECT)
                pygame.display.flip()
                pygame.time.wait(SHORTDELAY)
                pygame.draw.rect(screen, BGCOLOR, RECT)
                pygame.display.flip()
                pygame.time.wait(200)
            userInput = True
        else: # Have the player repeat the pattern
            if selected and selected == pattern[step]: # Correct color
                correct.play()
                pygame.draw.rect(screen, selected, RECT)
                pygame.display.flip()
                pygame.time.wait(SHORTDELAY)
                step += 1
                actionTime = time.time()

                if step == len(pattern): # Completed the pattern
                    correct.play()
                    pygame.draw.rect(screen, WHITE, RECT)
                    pygame.display.flip()
                    pygame.time.wait(SHORTDELAY)
                    userInput = False # Prepare to show a new pattern
                    level += 1 # increase the level
                    step = 0 # Reset step counter

            elif (selected and selected != pattern[step]): # Wrong color
                wrong.play()
                pattern = []
                step = 0
                userInput = False
                pygame.draw.rect(screen, BLACK, RECT)
                pygame.display.flip()
                pygame.time.wait(DELAY)

        pygame.display.update()
        clock.tick(30)

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        pygame.quit()
        sys.exit()
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        pygame.event.post(event) # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
