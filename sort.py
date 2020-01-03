
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

# button setup
bubbleSortButton = Button(window, black, 40, 80, 150, 30)
selectionSortButton = Button(window, black, 40, 120, 150, 30)
insertionSortButton = Button(window, black, 300, 80, 150, 30)
shuffleButton = Button(window, black, 300, 120, 150, 30)


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


def displayButtons():

	# window background to black
	window.fill((0,0,0))

	# grey background for menu
	pygame.draw.rect(window, grey, (0, 0, window_width, 180))

	# display title
	titleFont = pygame.font.Font('freesansbold.ttf', 40)
	titleSurface = titleFont.render('Sorting Visualizer', True, black)
	titleRect = titleSurface.get_rect()
	titleRect.center = ((window_width/2), 40)
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

	pygame.display.flip()


def displayBars(arr):

	barWidth = 20
	pos = 30

	# display the buttons
	displayButtons()

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

		# pygame.time.delay(100)

		# display before the sort
		displayBars(arr)

		bubbleSortButton.checkHover()
		insertionSortButton.checkHover()
		selectionSortButton.checkHover()
		shuffleButton.checkHover()

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
				if shuffleButton.checkClicked() == True:
					arr = buildArray()
					displayBars(arr)



def main():

	# generate random array
	arr = buildArray()

	# run the pygame
	runProgam(arr)
	pygame.quit()
	quit()


if __name__=='__main__':
	main()




