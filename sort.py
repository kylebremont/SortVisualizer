
import random
import pygame
import sort_algo
from button import Button

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
grey = (211,211,211)
green = (127,255,0)

# button setup
bubbleSortButton = Button(window, black, 15, 60, 150, 30)
selectionSortButton = Button(window, black, 175, 60, 150, 30)
insertionSortButton = Button(window, black, 335, 60, 150, 30)
shuffleButton = Button(window, black, 335, 120, 150, 30)
speedButton = Button(window, black, 40, 120, 90, 30)


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


def displayButtons(sortSpeed):

	# window background to black
	window.fill((0,0,0))

	# grey background for menu
	pygame.draw.rect(window, grey, (0, 0, window_width, 180))

	# display title
	titleFont = pygame.font.Font('freesansbold.ttf', 35)
	titleSurface = titleFont.render('Sorting Visualizer', True, black)
	titleRect = titleSurface.get_rect()
	titleRect.center = ((window_width/2), 30)
	window.blit(titleSurface, titleRect)

	# bubble sort button
	bubbleSortButton.setText('Bubble Sort')
	bubbleSortButton.draw()


	# selection sort button
	selectionSortButton.setText('Selection Sort')
	selectionSortButton.draw()

	# inserstion sort button
	insertionSortButton.setText('Insertion Sort')
	insertionSortButton.draw()

	# shuffle array button
	shuffleButton.setText('Shuffle Array')
	shuffleButton.draw()

	# change speed button
	speedButton.setText('Speed')
	speedButton.draw()

	# speed bar
	if sortSpeed == 5:
		pygame.draw.rect(window, green, (150, 120, 120, 30))
	else:
		pygame.draw.rect(window, black, (150, 120, 120, 30))
		pygame.draw.rect(window, green, (150, 120, 0.2*sortSpeed*120, 30))

def displayBars(arr, delay, sortSpeed):

	barWidth = 20
	pos = 30

	# display the buttons
	displayButtons(sortSpeed)

	# draw array
	for element in arr:
		barHeight = element.val
		pygame.draw.rect(window, element.color, (pos, 190, barWidth, barHeight))
		pos += 30

	# update window - this is the only place this happens
	pygame.display.flip()

	# only delay if called from sorting algorithms
	if delay == True:
		timeDelay = int(1/sortSpeed*1000)
		pygame.time.delay(timeDelay)


def runProgam(arr):

	sortSpeed = 1

	run = True
	while run:

		window.fill((0,0,0))
		# pygame.time.delay(100)

		# display before the sort
		displayBars(arr, False, sortSpeed)

		bubbleSortButton.checkHover()
		insertionSortButton.checkHover()
		selectionSortButton.checkHover()
		shuffleButton.checkHover()
		speedButton.checkHover()

		# events
		for event in pygame.event.get():
			# check if exit
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# check mouse clicked
			if event.type == pygame.MOUSEBUTTONDOWN:
				# if bubble sort clicked
				if bubbleSortButton.checkClicked() == True:
					sort_algo.Algorithm.bubbleSort(arr)
				# if selection sort clicked
				if selectionSortButton.checkClicked() == True:
					sort_algo.Algorithm.selectionSort(arr)
				# if insertion sort clicked
				if insertionSortButton.checkClicked() == True:
					sort_algo.Algorithm.insertionSort(arr)
				# if shuffle array clicked
				if shuffleButton.checkClicked() == True:
					arr = buildArray()
					displayBars(arr, False, sortSpeed)
				# if change speed clicked
				if speedButton.checkClicked() == True:
					if sortSpeed < 5:
						sortSpeed += 1
						sort_algo.sortSpeed += 1
					elif sortSpeed == 5:
						sortSpeed = 1
						sort_algo.sortSpeed = 1
					displayBars(arr, False, sortSpeed)



def main():

	# generate random array
	arr = buildArray()

	# run the pygame
	runProgam(arr)
	pygame.quit()
	quit()


if __name__=='__main__':
	main()




