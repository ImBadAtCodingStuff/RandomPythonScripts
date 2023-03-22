import pygame
import random
from time import sleep

# game speed
SPEED = 1


# Initialize Pygame
pygame.init()

# Define colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (2, 2, 2)
WHITE = (255, 255, 255)

# Define screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joystick Game")

# known button values
# A = 0
# B = 1
# X = 2
# Y = 3
# LB = 4
# RB = 5
# 2square = 6
# select = 7
# LSB = 8
# RSB = 9



# Define joystick buttons
BUTTON_A = 0
BUTTON_B = 1
BUTTON_X = 2
BUTTON_Y = 3
BUTTON_LB = 4
BUTTON_RB = 5
BUTTON_SQ = 6
BUTTON_SELECT = 7
BUTTON_LSB = 8
BUTTON_RSB = 9

BUTTON_EJECT = BUTTON_RB
BUTTON_HIGH = BUTTON_Y
BUTTON_MID = BUTTON_X
BUTTON_LOW = BUTTON_A
BUTTON_INTAKE = BUTTON_LB
BUTTON_ARM_DOWN = BUTTON_LSB
BUTTON_ARM_INTAKE = BUTTON_SELECT


# Define joystick axes
AXIS_X = 0
AXIS_Y = 1

# Initialize joystick
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def display_text(text1):
    # Create a font object
    font = pygame.font.Font(None, 36)

    # Render the text
    text = font.render(text1, True, WHITE)

    # Get the rect for the text surface
    text_rect = text.get_rect()

    # Center the text on the screen
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery

    # Fill the screen with black
    screen.fill(BLACK)

    # Blit the text onto the surface
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.update()

# Define game loop
def game_loop():
    while True:
        sleep(SPEED)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # reset screen
        screen.fill(BLACK)
        pygame.display.update()

        # Check if joystick is connected
        if joystick is None:
            continue

        # Get random action
        action = random.randint(0, 6)

        # good or bad
        win = True

        skip = False

        # Handle action
        if action == 0:  # Press eject
            #print("press A")
            display_text("press: HIGH")
            while not joystick.get_button(BUTTON_HIGH) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 1:  # Press high
            #print("press B")
            display_text("press: MID")
            while not joystick.get_button(BUTTON_MID) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 2:  # Press mid
            #print("press X")
            display_text("press: LOW")
            while not joystick.get_button(BUTTON_LOW) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 3:  # Press low
            #print("press Y")
            display_text("press: EJECT")
            while not joystick.get_button(BUTTON_EJECT) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 4:  # Press low
            #print("press Y")
            display_text("press: INTAKE")
            while not joystick.get_button(BUTTON_INTAKE) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 5:  # Press low
            #print("press Y")
            display_text("press: ARM DOWN")
            while not joystick.get_button(BUTTON_ARM_DOWN) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)
        elif action == 6:  # Press low
            #print("press Y")
            display_text("press: ARM INTAKE")
            while not joystick.get_button(BUTTON_ARM_INTAKE) and not skip:
                for event in pygame.event.get():
                    print(event.type)
                    if event.type == 1540:
                        screen.fill(RED)
                        win = False
                        skip = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if win:
                screen.fill(GREEN)

        # Update the screen
        pygame.display.update()
        print("sleeping")
        #sleep(1)

# Start the game
if joystick is not None:
    display_text("Press A to start")
    while not joystick.get_button(BUTTON_A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    display_text("Starting...")
    game_loop()
else:
    print("No joystick found")
