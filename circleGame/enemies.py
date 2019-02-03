from settings import Settings
import random
from random import randint as rd
from player import Player
import pygame


class Enemy():
	speed = 1 #bigger speed, slower enemy
	def __init__(self):
		self.age = 0
		self.randomlala = rd(0, 3)

		if self.randomlala == 0:
			self.xCoord = rd(0, Settings.screenWidth)
			self.yCoord = 0
		elif self.randomlala == 1:
			self.xCoord = 0
			self.yCoord = rd(0, Settings.screenHeight)
		elif self.randomlala == 2:
			self.xCoord = rd(0, Settings.screenWidth)
			self.yCoord = Settings.screenHeight
		elif self.randomlala == 3:
			self.xCoord = Settings.screenWidth
			self.yCoord = rd(0, Settings.screenHeight)

		self.size = rd(round(Player.size * 0.25), round(Player.size * 2))

		#self.size = rd(round(Player.size * 0.25), round(Player.size * 1.3))

		self.color = (rd(20, 255), rd(20, 255), rd(20, 255))

		self.randomVector = [rd(-1, 1), rd(-1, 1)]
		

	def move(self):
		self.xCoord += self.randomVector[0]
		self.yCoord += self.randomVector[1]
		self.age += 1

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.xCoord, self.yCoord], round(self.size))
	def shrink(self, stage):
		self.size /= stage


