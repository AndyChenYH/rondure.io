import random
class Settings():
	colors = {
		'BLACK': (  0,   0,   0),
		'WHITE': (255, 255, 255),
		'BLUE': (  0,   0, 255),
		'GREEN': (  0, 255,   0),
		'RED': (255,   0,   0),
		'CYAN': (100, 100, 255)
	}

	gameName = 'Rondure.io'
	screenWidth = 2600
	screenHeight = 1600
	backgroundColor = colors['BLACK']
	quit = False
	killedBy = None
	stage = 1
	pause = False

	def randomName():
		firstName = ['John', 'Donald', 'James', 'Robert', 'Micheal', 'William', 'Charles', 'Joseph', 'Daniel', 'Paul']
		lastName = ['Smith', 'Johnson', 'Trump', 'Williams', 'Jones', 'Brown', 'Davis', 'Moore', 'Taylor', 'Thomas']

		return random.choice(firstName) + " " + random.choice(lastName)

	def stageToObject(stage):
		return [
			'an E Coli',
			'a White Blood Cell',
			'a Human Sperm',
			'a Human Egg',
			'a Paramecium',
			'an Amoeba',
			'the Largest Bacteria',
			'an Ant',
			'a Common EarthWorm',
			'a Shrew',
			'a Dodo Bird',
			'a Human',
			'a Giant Earthworm',
			'a Tyrannosaurus Rex',
			'a Blue Whale',
			'the Titanic',
			'the Half Dome',
			'the Central Park',
			"Halley's Comet",
			'Rhode Island',
			'California',
			'The Moon',
			'The Earth',
			'Jupiter',
			'The Sun',
			'The Vega Star',
			'Total Human Height',
			'Polaris',
			'Distance Earth To Sun',
			'Antares',
			'Betelguese',
			'Distance Neptune To Sun',
			'One Light Day',
			'Homunculus Nebula',
			'StingRay Nebula',
			"Cat's Eye Nebula",
			'One Light Year',
			'Ant Nebula',
			'Bubble Nebula',
			'Orion Nebula',
			'Omega Centauri',
			'Tarantula Nebula',
			'Small Magellanic Cloud',
			'Sombrero Galaxy',
			'Milky Way Galaxy',
			'Virgo A',
			'Distance Earth Travelled',
			'Distance To Andromeda',
			'Local Group',
			'Virgo Cluster',
			'Virgo Supercluster',
			'Eridanus Supervoid',
			'Sloan Great Wall',
			'Distance to Hubble DeepField',
			'Obserable Universe',
			'5.4*10^61 plank lengths',
		][stage-1]


