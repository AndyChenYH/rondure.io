from settings import Settings

class Player():

	xCoord = int(Settings.screenWidth / 2)
	yCoord = int(Settings.screenHeight / 2)
	size = 20
	actualSize = 20
	color = Settings.colors['WHITE']
	speed = 0.0001 #smaller the number, faster the player

	def shrink(stage):
		size /= stage



