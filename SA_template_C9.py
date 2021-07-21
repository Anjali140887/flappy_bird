import pygame, sys
pygame.init()
clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
images={}
images["bg1"] = pygame.image.load("D:/Flappy for AI/bg1.png").convert_alpha()
images["base"] = pygame.image.load("D:/Flappy for AI/base.png").convert_alpha()
while True:
    screen.fill((50,150,255))
    screen.blit(images["bg1"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(images["base"],[0,550])
    pygame.display.update()
    
pygame.quit()
{"mode":"full","isActive":false}
