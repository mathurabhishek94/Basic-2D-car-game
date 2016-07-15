

import pygame
from startmenu import *
from BaseClass import * 
pygame.init()
screensize=(720,540)
gamename="Mid-Town Madness"
screen=pygame.display.set_mode(screensize)
pygame.display.set_caption(gamename)
#start menu of the game
menu=startmenu(screen)
while True:
	if menu.startgame==True:
		break
#start menu of the game

pygame.mixer_music.load("gamesong.mp3")
pygame.mixer_music.play(3,0.0)
clock=pygame.time.Clock()
FPS=10
grassbackground=(120,250,0)
roadbackground=(255,255,255)
roaddivider=(0,0,0)
roadwidth=360
dividernum=10
dividerwidth=10
dividerheight=54
screen.fill(grassbackground)

mycar=Car(330,420,65,110,"images/redcar.jpg")
incomming=IncommingCar(65,110,"images/flippedbluecar.jpg")

def wearedone():
	screen.fill((255,255,255))
	
	#displayscore
	font = pygame.font.SysFont( None, 45)
	text1=font.render("YOU CRASHED !",True,(0,0,0))
	text2=font.render("Score: "+str(IncommingCar.score) ,True , (0,0,0))
	screen.blit(text1,(10,0))
	screen.blit(text2,(10,40))
	#displayscore
	IncommingCar.score=0
	pygame.display.flip()
	pygame.time.delay(5000)


#---------------main game loop-------------------

while True:
		#processing
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		keyspressed=pygame.key.get_pressed()
		if keyspressed[pygame.K_a]:
			mycar.velx=-10
		elif keyspressed[pygame.K_d]:
			mycar.velx=10
		else:
			mycar.velx=0	
		#processing
		
		#logic 
		mycar.movecar()
		incomming.motion()
		while True:
			while i<=540-dividerheight+10:
				pygame.draw.rect(screen,roaddivider,(170+180,i,dividerwidth,dividerheight))
				i+=dividerheight+10
			if (mycar.rect.y==incomming.rect.y+110) and	 (incomming.rect.x< mycar.rect.x < incomming.rect.x+65 or
		 			incomming.rect.x< mycar.rect.x+65 < incomming.rect.x+65):
		 			break
		 	i+=	

		if (mycar.rect.y==incomming.rect.y+110) and	 (incomming.rect.x< mycar.rect.x < incomming.rect.x+65 or
		 incomming.rect.x< mycar.rect.x+65 < incomming.rect.x+65):
			wearedone()
			break

		if IncommingCar.score==3 or IncommingCar.score==8 or IncommingCar.score==14:
			FPS+=1

		#logic
		
		#drawing
		pygame.draw.rect(screen,roadbackground,(180,0,roadwidth,540))
		i=0
		
		Car.ListOfAllSprites.draw(screen)
		font = pygame.font.SysFont( None, 25)
		text=font.render("Score: "+ str(IncommingCar.score) ,True , (255,255,255))
		screen.blit(text,(0,0))
		pygame.display.flip()
		#drawing
		clock.tick(FPS)

  



