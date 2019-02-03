import pygame
import sys
import time
from settings import Settings
from enemies import Enemy
from player import Player
from random import randint as rd


def checkBoundary(theThing): #returns T/F whether out or in
	left = theThing.xCoord > 0
	right = theThing.xCoord < Settings.screenWidth
	up = theThing.yCoord > 0
	down = theThing.yCoord < Settings.screenHeight
	return left and right and up and down

def checkEvents(player=Player):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p: #pausing
				if Settings.pause == False:
					Settings.pause = True
				elif Settings.pause == True:
					Settings.pause = False

def checkCollision(player, enemyList):
	for enemy in enemyList:
		deltaX = abs(enemy.xCoord - player.xCoord)
		deltaY = abs(enemy.yCoord - player.yCoord)
		if (((deltaX ** 2) + (deltaY ** 2)) ** (1/2)) < (enemy.size + player.size - (player.size * 0.6)): #touching enemy
			if player.size - player.size * 0.1 > enemy.size:
				player.size += 1
				player.actualSize += 1
				enemyList[enemyList.index(enemy)] = Enemy()	

			elif (enemy.size - player.size * 0.1 > player.size) and (enemy.age > 50):
				print(enemy.color)
				Settings.quit = True
				Settings.killedBy = enemy

def restartGame(screen):
	screen.fill(Settings.colors['BLACK'])
	Settings.quit = False
	Player.size = 20
	Player.actualSize = 20
	Settings.killedBy = None
	Settings.stage = 1


def nextTerm(enemyList):
	if 110 < Player.size:
		Settings.stage += 1
		Player.size = 20
		for enemy in enemyList:
			enemy.size = rd(round(Player.size * 0.25), round(Player.size))
			# enemy.size = rd(round(Player.size * 0.25), round(Player.size * 1.3))
			enemy.age = 0
