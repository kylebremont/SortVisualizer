

import pygame


# colors
red = (255,0,0)
white = (255,255,255)
purple = (255,0,255)
black = (0,0,0)
grey = (211,211,211)
blue = (0,191,255)
darkgrey = (105,105,105)



# These 2 functions are the same with the colour of the text being the exception.  its renders the text and its color
def text_objects (text, font, color): 
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()


class Button:

	def __init__(self, window, color, x, y, width, height):
		self.body = pygame.Rect(x, y, width, height)
		self.window = window
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color

	def setText(self, buttonText):
		self.text = buttonText

	def checkClicked(self):
		mousePos = pygame.mouse.get_pos()
		x, y = 0, 1
		if self.x + self.width > mousePos[x] > self.x and self.y + self.height > mousePos[y] > self.y:
			return True
		else:
			return False

	def Hover(self, color):
		self.color = color
		self.draw()

	def checkHover(self):
		mousePos = pygame.mouse.get_pos()
		x, y = 0, 1
		if self.x + self.width > mousePos[x] > self.x and self.y + self.height > mousePos[y] > self.y:
			self.Hover(darkgrey)
		else:
			self.Hover(black)

	def draw(self):
		buttonFont = pygame.font.Font('freesansbold.ttf', 20)
		textSurf, textRect = text_objects(self.text, buttonFont, grey)
		textRect.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))

		pygame.draw.rect(self.window, self.color, self.body)
		self.window.blit(textSurf, textRect)


