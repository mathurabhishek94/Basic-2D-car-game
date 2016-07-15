
#List of All the classes in the game

import pygame
from random import randint,randrange
class Car(pygame.sprite.Sprite):
	ListOfAllSprites=pygame.sprite.Group()
	def __init__(self,xpos,ypos,width,height,imagestring):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagestring)
		self.rect=self.image.get_rect()
		self.rect.x=xpos
		self.rect.y=ypos
		self.width=width
		self.height=height
		Car.ListOfAllSprites.add(self)
		self.velx=5
		self.vely=0

	def movecar(self):
		carpos=self.rect.x+self.velx
		if (180)<=carpos<=(720-180-65):
			self.velx=self.velx
		else:
			self.velx=0
		self.rect.x+=self.velx

class IncommingCar(Car):
	score=0
	def __init__(self,width,height,imagestring):
		self.spawnposx=randint(180,360-65+180)
		self.spawnposy=2
		Car.__init__(self,self.spawnposx,self.spawnposy,
			width,height,imagestring)
		self.velx=0
		self.vely=5

		

	def motion(self):
		self.rect.y+=self.vely
		if(self.rect.y>600):
			self.rect.y=0-110
			self.rect.x=randrange(180,295+180)
			IncommingCar.score+=1





		




















