import pygame                           
pygame.init()
WIDTH = 420
HEIGHT= 420
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

''' Initialize RGB colours'''
RED  =(  255,  0,  0) 
BLUE =(  0,  0,  255)
WHITE= (  255,  255,  255)
OUTLINE=0


brick_x=  200
brick_y=  200
brick_w = 20
brick_h = 20
speed_x = 2
speed_y = 2


in_play = True

while in_play:
    game_window.fill(WHITE)
    pygame.draw.rect(game_window, RED, (brick_x, brick_y, brick_w, brick_h), OUTLINE)
    pygame.display.update()
    pygame.time.delay(4)


    pygame.event.get()                  
    keys = pygame.key.get_pressed()     
	

    if keys[pygame.K_ESCAPE]:           
        in_play = False
        
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]: 
         speed_x=0
         if keys[pygame.K_COMMA]:
             if brick_x!=0: 
                 speed_x=1
                 brick_x = brick_x - speed_x
                 if brick_x<=0 : 
                      speed_x=0    
         elif brick_x!=0: 
             speed_x=2
             brick_x = brick_x - speed_x
             if brick_x<=0: 
                  speed_x=0        
                    
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
         if keys[pygame.K_COMMA]:
             if brick_x!=400: 
                 speed_x=1
                 brick_x = brick_x + speed_x
                 if brick_x>=400 : 
                     speed_x=0  
         if brick_x!=400: 
             speed_x=2
             brick_x = brick_x + speed_x 
             if brick_x==400:
                 speed_x=0
          
    elif keys[pygame.K_UP] or keys[pygame.K_w]: 
        if keys[pygame.K_COMMA]:
             if brick_y!=0: 
                 speed_y=1
                 brick_y = brick_y - speed_y
                 if brick_y<=0 : 
                     speed_y=0   
        
             elif brick_x!=0:
                 speed_y=2
                 brick_y = brick_y-speed_y 
                 if brick_y==0:
                     speed_y=0 

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]: 
        if keys[pygame.K_COMMA]:
             if brick_y!=400: 
                 speed_y=1
                 brick_y = brick_y - speed_y
                 if brick_y==400 : 
                     speed_y=0  
        if brick_y!=400:
             speed_y=2
             brick_y = brick_y + speed_y
             if brick_y==400:
                 speed_y=0
