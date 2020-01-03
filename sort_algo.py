
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
				sort.displayBars(arr, True)
				# swap elements, change color, redisplay
				arr[j+1].color, arr[j].color = white, white
				arr[j+1] = arr[j]
				sort.displayBars(arr, True)
				j -= 1
			arr[j+1].val = key.val
			sort.displayBars(arr, True)


	def selectionSort(arr):

		# selection sort algorithm
		n = len(arr)
		for i in range(n):
			min_idx = i
			arr[i].color = red
			for j in range(i+1, n):
				if arr[min_idx].val > arr[j].val:
					# change color of current unsorted min to red and change previous unsorted min to white, redisplay
					if min_idx != i:
						arr[min_idx].color = white
					arr[j].color = red
					sort.displayBars(arr, True)
					# update minimum index
					min_idx = j

			# if the bar at i is not the smallest unsorted bar, change colors to green
			if min_idx != i:
				arr[i].color, arr[min_idx].color = green, green
				sort.displayBars(arr, True)
			# change color of sorted bar to purple, swap and redisplay
			arr[i].color, arr[min_idx].color = white, purple
			arr[i], arr[min_idx] = arr[min_idx], arr[i]
			sort.displayBars(arr, True)


	def bubbleSort(arr):

		# bubble sort algorithm
		n = len(arr)
		for i in range(n):
			for j in range(0, n-i-1):
				# change color to red and redisplay for every comparison
				arr[j].color, arr[j+1].color = red, red
				sort.displayBars(arr, True)
				# if there is a swap
				if arr[j].val > arr[j+1].val:
					# change color to green if swap occurs and redisplay
					arr[j].color, arr[j+1].color = green, green
					sort.displayBars(arr, True)
					# swap elements
					arr[j], arr[j+1] = arr[j+1], arr[j]
				# change color back to white and redisplay
				arr[j].color, arr[j+1].color = white, white
				sort.displayBars(arr, True)

			# once that bar is sorted, change the color to purple
			arr[j+1].color = purple
			sort.displayBars(arr, True)
		arr[0].color = purple
		sort.displayBars(arr, True)

