import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)

# Set up the Pygame clock
clock = pygame.time.Clock()

# Initialize the Pygame joystick
pygame.joystick.init()

# Set up the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Main game loop
while True:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the player closes the window
            pygame.quit()
            quit()

    # Get the state of each button on the joystick
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            print("Button", i, "is pressed.")

    # Limit the game to 60 frames per second
    clock.tick(60)
