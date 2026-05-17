import Pygame

Pygame.init()
#create the display surface object of specific dimension
window = Pygame.set_mode((400, 300))
#fill the surface with a color to make it visible
window.fill((255, 255, 255))
#define a color
GREEN = (0, 255, 0)
#draw a solid circle on the surface
Pygame.draw.circle(window, GREEN, (200, 150), 50)
#draw outlined circle 
Pygame.draw.line(window, (0, 0, 255), (100, 100), 5)
#draw the surface object to the screen
Pygame.display.update()
#game loop
running = True

while running:
    #event handling
    for event in Pygame.event.get():
        if event.type == Pygame.QUIT:
            running = False
            #Quit Pygame
Pygame.quit()