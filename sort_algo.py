
import sort

# colors
red = (255,0,0)
white = (255,255,255)
purple = (255,0,255)
black = (0,0,0)
green = (127,255,0)

class Algorithm:

	# THIS DOESN'T WORK RIGHT NOW
	def insertionSort(arr):

		# insertion sort algorithm
		n = len(arr)
		for i in range(1, n):

			key = arr[i]
			j = i-1
			while j >= 0 and key.val < arr[j].val:
				# change color and redisplay
				arr[j+1].color, arr[j].color = red, red
				sort.displayBars(arr)
				# swap elements, change color, redisplay
				arr[j+1].color, arr[j].color = white, white
				arr[j+1] = arr[j]
				sort.displayBars(arr)
				j -= 1
			arr[j+1].val = key.val
			sort.displayBars(arr)


	def selectionSort(arr):

		# selection sort algorithm
		n = len(arr)
		for i in range(n):
			min_idx = i
			for j in range(i+1, n):
				if arr[min_idx].val > arr[j].val:
					min_idx = j

			if min_idx != i:
				# change color and redisplay
				arr[i].color, arr[min_idx].color = red, red
				sort.displayBars(arr)
				# swap elements, change color, redisplay
				arr[i].color, arr[min_idx].color = white, white
				arr[i], arr[min_idx] = arr[min_idx], arr[i]
				sort.displayBars(arr)


	def bubbleSort(arr):

		# bubble sort algorithm
		n = len(arr)
		for i in range(n):
			for j in range(0, n-i-1):
				# change color to red and redisplay for every comparison
				arr[j].color, arr[j+1].color = red, red
				sort.displayBars(arr)
				# if there is a swap
				if arr[j].val > arr[j+1].val:
					# change color to green if swap occurs and redisplay
					arr[j].color, arr[j+1].color = green, green
					sort.displayBars(arr)
					# swap elements
					arr[j], arr[j+1] = arr[j+1], arr[j]
				# change color back to white and redisplay
				arr[j].color, arr[j+1].color = white, white
				sort.displayBars(arr)

			# once that bar is sorted, change the color to purple
			arr[j+1].color = purple
			sort.displayBars(arr)
		arr[0].color = purple
		sort.displayBars(arr)

