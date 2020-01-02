
import random
import pygame
import sort_algo

# pygame window setup
pygame.init()
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Sort Visualizer')

# colors
red = (255,0,0)
white = (255,255,255)
purple = (255,0,255)
black = (0,0,0)


# class for each array element
class arrElement:

	def __init__(self, val, color):
		self.val = val
		self.color = color


# generates a random array of size 15
def buildArray():

	arr = []
	backgroundColor = (255, 255, 255)
	for i in range(15):
		rand = random.randrange(75, 300)
		arr.append(arrElement(rand, backgroundColor))

	return arr

# text_objects, displayControls, and displayBars all contribute to display
def text_objects(text, font):

	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()


def displayControls():

	# display title
	titleFont = pygame.font.Font('freesansbold.ttf', 40)
	titleSurface, titleRect = text_objects('Sorting Visualizer', titleFont)
	titleRect.center = ((window_width/2), 50)
	window.blit(titleSurface, titleRect)

	# first control
	controlFont = pygame.font.Font('freesansbold.ttf', 25)
	control1Surf, control1Rect = text_objects('1: Bubble Sort', controlFont)
	control1Rect.center = (100, 100)
	window.blit(control1Surf, control1Rect)

	# second control
	controlFont = pygame.font.Font('freesansbold.ttf', 25)
	control1Surf, control1Rect = text_objects('2: Selection Sort', controlFont)
	control1Rect.center = (115, 130)
	window.blit(control1Surf, control1Rect)

	# third control
	controlFont = pygame.font.Font('freesansbold.ttf', 25)
	control1Surf, control1Rect = text_objects('3: Insertion Sort', controlFont)
	control1Rect.center = (111, 160)
	window.blit(control1Surf, control1Rect)

	# fourth control
	controlFont = pygame.font.Font('freesansbold.ttf', 25)
	control1Surf, control1Rect = text_objects('s: Shuffle Array', controlFont)
	control1Rect.center = (350, 100)
	window.blit(control1Surf, control1Rect)


def displayBars(arr):

	barWidth = 20
	pos = 30

	# window background to black
	window.fill((0,0,0))
	displayControls()

	# draw array
	for element in arr:
		barHeight = element.val
		pygame.draw.rect(window, element.color, (pos, 190, barWidth, barHeight))
		pos += 30
	pygame.display.flip()
	pygame.time.delay(500)


def runProgam(arr):

	run = True
	while run:

		pygame.time.delay(100)

		# display before the sort
		displayBars(arr)

		# events
		for event in pygame.event.get():
			# check if exit
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# check keypressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					# rebuild the array and redisplay
					arr = buildArray()
					displayBars(arr)
				if event.key == pygame.K_1:
					# call bubble sort
					sort_algo.Algorithm.bubbleSort(arr)
				if event.key == pygame.K_2:
					# call selection sort
					sort_algo.Algorithm.selectionSort(arr)
				if event.key == pygame.K_3:
					# call insertion sort
					sort_algo.Algorithm.insertionSort(arr)



def main():

	# generate random array
	arr = buildArray()

	# run the pygame
	runProgam(arr)
	pygame.quit()
	quit()


if __name__=='__main__':
	main()




