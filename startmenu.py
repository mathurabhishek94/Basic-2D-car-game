import pygame,sys

class startmenu():
	def __init__(self,screen):
		self.startgame=False
		self.quitgame=False
		bgimage=pygame.image.load("images\startmenubg.jpg")
		screen.blit(bgimage,(0,0))
		startbutton=pygame.image.load("images\startbutton.png")
		screen.blit(startbutton,(260,270))
		clock=pygame.time.Clock()
		
		while self.startgame==False:
			for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit()
						sys.exit()	
			mpos=pygame.mouse.get_pos()
			if 260<mpos[0]<260+174 and 270<mpos[1]<270+64:
				if pygame.mouse.get_pressed()[0]:
					self.startgame=True	
			pygame.display.flip()
			clock.tick(15)

			
			
			