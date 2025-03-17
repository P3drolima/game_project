import pygame


pygame.init()

# Creating surface
window = pygame.display.set_mode(size=(600, 480))

while True:
    # Check for all events from queue
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()   # Close Window
            quit() # End pygame