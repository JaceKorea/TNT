import pygame
import sys
from pygame.locals import *

import time
   
pygame.init ( )

xs=-50
ys=0
jup=0
f=10
sec=1

screen=pygame.display.set_mode((800,600))

paddle=pygame.Rect(930, 900,30, 70)
paddle_dy=60
paddle_dx=0

bricks=[pygame.Rect(60+ 200*i, 999+200*j, 200, 19)for i in range(10) for j in range(1)]

def game_over( ):
	draw_text("GAME OVER", 48, screen.get_width( ) / 2, screen.get_height( ) / 2)
	pygame.display.flip( )
	pygame.time.wait(3000)
	pygame.quit( )
	sys.exit( )

while True:
	for event in pygame.event.get( ):
		if event.type==pygame.QUIT:
			pygame.quit ( )
			sys. exit( )
		
	keys=pygame.key.get_pressed( )
	if keys[pygame.K_LEFT] :
         xs -= 2
	if keys[pygame.K_RIGHT] :
		 xs += 2
	if keys[pygame.K_UP] and hit_index !=-1:
		jup=15
		
	hit_index = paddle.collidelist(bricks)
						
	if jup>0:
		ys-=3
		jup=jup-1
			
	paddle.top += paddle_dy
			
	paddle_dy =ys		
	if ys<30:
		ys=ys+1
		if hit_index !=-1:
			paddle.top-=2 				
		
																
	paddle.left=paddle.left+xs
		
	screen. fill((0,0,0))
	pygame.draw.rect(screen, (50,255,255), paddle)
	for brick in bricks:
			pygame.draw.rect(screen, (250, 250, 250), brick)
				 
	pygame.display.flip( )
			
	if hit_index !=-1:	
		ys=0		
	
	xs*=0.9
	
	pygame.time.delay(10)
