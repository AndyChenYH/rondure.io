import pygame
import sys
import time
from settings import Settings
from player import Player
from enemies import Enemy
import gameFunctions as gf
from random import randint as rd
import scene

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 80)
screen = pygame.display.set_mode([Settings.screenWidth, Settings.screenHeight])
pygame.display.set_caption(Settings.gameName)

def playGame(screen, myfont):
	scene.starting(screen, myfont)

	enemyList = [Enemy() for i in range(50)] #difficulty
	iterations = 0
	while True:
		screen.fill(Settings.backgroundColor)
		if not Settings.pause:
			Player.xCoord, Player.yCoord = pygame.mouse.get_pos() #delete this line to use keys 
		pygame.draw.circle(screen, Player.color, [Player.xCoord, Player.yCoord], round(Player.size)) #draws the Player
		for enemy in enemyList:
			enemy.draw(screen)
			if (not Settings.pause) and (iterations % enemy.speed == 0):
				enemy.move() #makes enemies move in a set direction(determined from the __init__() function)
		for enemy in enemyList:
			if not gf.checkBoundary(enemy):
				enemyList[enemyList.index(enemy)] = Enemy()
		time.sleep(Player.speed)
		gf.checkEvents(Player)
		gf.checkCollision(Player, enemyList)
		textsurface = myfont.render('Size: ' + str(round(Player.actualSize)) + 
									" " * 30 + 
									"About the width of : " 
									+ str(Settings.stageToObject(Settings.stage)), False, 
									Settings.colors['WHITE']) #shows score
		screen.blit(textsurface,(0,0))
		gf.nextTerm(enemyList)
		pygame.display.flip()
		if Settings.quit:
			break
		iterations += 1
	scene.endCredits(screen, myfont)

#main game loop
while True:
	playGame(screen, myfont)
	gf.restartGame(screen)
