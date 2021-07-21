import pygame, sys
pygame.init()
clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
## Space for the code to be written ##
while True:
    screen.fill((50,150,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   
    pygame.display.update()
    
pygame.quit()
