import pygame
 
FPS = 60
W = 700  
H = 700  
WHITE = (255, 255, 255)
BLUE = (0, 0, 225)

UP = "up"
DOWN = "down"
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
x = W // 2
y = H // 2
r = 50

speed = 20

motion = STOP
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                motion = LEFT
            elif i.key == pygame.K_d:
                motion = RIGHT
            elif i.key == pygame.K_w:
                motion = UP
            elif i.key == pygame.K_s:
                motion = DOWN
            elif  i.key == pygame.K_ESCAPE:
                exit()
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]:
                motion = STOP
 
    if motion == LEFT:
        x -= speed
    elif motion == RIGHT:
        x += speed
    elif motion == UP:
        y -= speed
    elif motion == DOWN:
        y += speed
    
#1 from another side

    #if x >= W + r:
     #   x = 0 - r
    #elif x <= 0 - r:
     #   x = W + r
    #elif y >= H + r:
     #   y = 0 - r
    #elif y <= 0 - r:
     #   y = H + r

#2 stop

    #if x == W - r:
     #   motion = STOP
    #elif x == 0 + r:
     #   motion = STOP
    #elif y >= H -r:
     #   motion = STOP
    #elif y <= 0 + r:
     #   motion = STOP

#3 change direction
    
    if x + r > W  or x < 0 + r: 
        speed = speed*(-1)
    if y + r > H  or y < 0 + r:
        speed = speed*(-1)


    clock.tick(FPS)



pygame.quit()