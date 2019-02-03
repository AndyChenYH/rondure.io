from random import randint as rd
import math


def normalDistribution(x):
	return (1/(math.sqrt(2*math.pi))) * (math.e ** -((x ** 2)/2))

def randomZScore():
	while True:
		randX = rd(-30000, 30000) / 10000
		randY = rd(0, 50000) / 100000

		if randY <= normalDistribution(randX):
			return randX
print(randomZScore())
