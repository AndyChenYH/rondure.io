import pygame
from settings import Settings
from player import Player
import time
import sys

def starting(screen, myFont):
	done = False
	screen.fill(Settings.colors['BLACK'])
	while not done:
		textSurface = myFont.render('Press space to start...', False, Settings.colors['WHITE'])

		screen.blit(textSurface,(400, 400))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					done = True

		pygame.display.flip()

def endCredits(screen, myFont):

		time.sleep(1)
		screen.fill(Settings.colors['BLACK'])
		textSurface = myFont.render("You final size was %d..." % Player.actualSize, False, Settings.colors['WHITE'])
		screen.blit(textSurface, (400, 400))
		pygame.display.flip()
		time.sleep(1)

		screen.fill(Settings.colors['BLACK'])
		textSurface = myFont.render("Everything made by Andy Chen", False, Settings.colors['WHITE'])
		screen.blit(textSurface, (400, 400))
		pygame.display.flip()
		time.sleep(0.3)

		screen.fill(Settings.colors['BLACK'])
		textSurface = myFont.render("killed by: " + Settings.randomName(), False, Settings.colors['WHITE'])
		Settings.killedBy.draw(screen)
		screen.blit(textSurface, (300, 400))
		pygame.display.flip()
		time.sleep(1)


		


