import pygame, sys
pygame.init()
clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
images={}
images["bg1"] = pygame.image.load("C:/Users/NASCA/Desktop/Flappy for AI/Flappy for AI/bg1.png").convert_alpha()
images["base"] = pygame.image.load("C:/Users/NASCA/Desktop/Flappy for AI/Flappy for AI/base.png").convert_alpha()
images["bird"] = pygame.image.load("C:/Users/NASCA/Desktop/Flappy for AI/Flappy for AI/bird.png").convert_alpha()
class Bird:
    r=pygame.Rect(100,250,30,30)
    speed=0
    g=0.5
while True:
    screen.fill((50,150,255))
    screen.blit(images["bg1"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(images["base"],[0,550])
    pygame.display.update()
    
pygame.quit()
