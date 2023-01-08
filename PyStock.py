"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 1/7/2023
	Project name: PyStock
	File name: PyStock.py
	File description: This file is the project's main file, running a Stock Market GUI using Pygame and the YFinance modules (see requirements.txt for a full list of third-party modules).
"""
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Hide the Pygame welcome message.

# Python Standard Library and Third-Party Module imports.
import pygame, sys, time, random, subprocess
from pygame.locals import *

# Project file imports.
from Financing import *

pygame.init() # Initialize the Pygame.

""" Define colors """
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)

""" Create basic rendering functions. """
def drawText(text, font, surface, x, y, COLOR=BLACK):
	""" Draw text onto the passed surface with the given font and location """
	textobj = font.render(text, 1, COLOR) # Create the text as an object, 
	textrect = textobj.get_rect() # Create the rect for the object.
	textrect.topleft = (x, y) # Position the rect at the passed coordinates.
	surface.blit(textobj, textrect) # Display the object using its assigned rect.
def drawRed(text, font, surface, x, y):
	""" Draw red text onto the passed surface with the given font and location """
	textobj = font.render(text, 1, RED)# Create the text as an object, 
	textrect = textobj.get_rect() # Create the rect for the object.
	textrect.topleft = (x, y) # Position the rect at the passed coordinates.
	surface.blit(textobj, textrect) # Display the object using its assigned rect.
def drawGreen(text, font, surface, x, y):
	""" Draw green text onto the passed surface with the given font and location """
	textobj = font.render(text, 1, GREEN)# Create the text as an object, 
	textrect = textobj.get_rect() # Create the rect for the object.
	textrect.topleft = (x, y) # Position the rect at the passed coordinates.
	surface.blit(textobj, textrect) # Display the object using its assigned rect.

""" Create a sprite creation function """
def Spr(ImageName):
	""" Load the image into a pygame.image object and a rect object """
	return pygame.image.load(f'images/{ImageName}.png'), pygame.image.load(f'images/{ImageName}.png').get_rect()

# The main function
def PYSTOCK():
	""" The main project function, a GUI for interacting with the Yahoo Finance API and rendering the requested stock data as a graph. """
	WINDOWWIDTH = 1000
	WINDOWHEIGHT = 700
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Create the window.
	pygame.display.set_caption('PyStock') # Set the window caption.
	Surface = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT) # Create the surface rect object.
	Pystock_icon = pygame.transform.scale(pygame.image.load("images/Blank.png"), (32, 32)) # Create and resize the PyStock Icon.
	pygame.display.set_icon(Pystock_icon) # Set it as the window icon.
	
	""" Sprites or images for various buttons and displays """
	pystockLogo, pystockLogo_rect = Spr("PystockLogo")
	buttonImage, buttonImage_rect = Spr("PystockChoices")
	DOW_and_NAS, DOW_and_NAS_rect = Spr("DowAndNasdaq") # The icon for beside the Dow Jones and NASDAQ data.
	textInputBoxBlank, TRect = Spr("Ticker_with_message") # The text input box (active)
	textInputBoxActive, TRect = Spr("Ticker_blank") # The text input box (inactive)
	Search, SearchRect = Spr("Search") # The search button.
	Add, AddRect = Spr("AddTicker") # The button to add a ticker to the tickerlist.
	tickerListBox, tickerListBoxRect = Spr("tickerListBox") # The tickerlist box.
	
	""" Popular stock icons """
	Disney, DisneyRect = Spr("Disney")
	Apple, AppleRect = Spr("Apple")
	Google, GoogleRect = Spr("Google")
	Amazon, AmazonRect = Spr("Amazon")
	Facebook, FacebookRect = Spr("Facebook")
	Netflix, NetflixRect = Spr("Netflix")

	""" Reposition images and sprites relative to the Surface object. """
	TRect.midbottom = Surface.midbottom
	TRect.bottom-=15
	buttonImage_rect.center = Surface.center
	buttonImage_rect.centery+=30
	pystockLogo_rect.centerx = Surface.centerx # The PyStock logo.
	DOW_and_NAS_rect.right = Surface.right # The Dow and NASDAQ display icon.
	SearchRect.centery = TRect.centery # The search button.
	SearchRect.left = TRect.right+25
	AddRect.topleft = SearchRect.topright # The tickerlist add button.
	AddRect.left += 25
	tickerListBoxRect.topleft = (Surface.right-165, Surface.centery-15) # The tickerlist box.
	DisneyRect.top = pystockLogo_rect.bottom # The popular stock icons.
	DisneyRect.left = 25
	AppleRect.top = DisneyRect.bottom+25
	AppleRect.left = 25
	GoogleRect.top = AppleRect.bottom+25
	GoogleRect.left = 25
	AmazonRect.top = GoogleRect.bottom+25
	AmazonRect.left = 25
	FacebookRect.top = AmazonRect.bottom+25
	FacebookRect.left = 25
	NetflixRect.top = FacebookRect.bottom+25
	NetflixRect.left = 25
	
	""" Create various application resources """
	largeFont = pygame.font.SysFont(None, 50) # Larger text font.
	font = pygame.font.SysFont(None, 22) # Smaller text font.
	mainClock = pygame.time.Clock() # Application clock.
	SquareSize = 126
	Selected = "max"
	textTicker = ""
	tickerList = []
	EvenOrOdd = 1
	TYPING = False
	
	""" Get the market data for the Dow Jones and the NASDAQ for the prior day """
	NAS_Change, NAS_Close, NAS_Percent = getNASDAQDay()
	DOW_Change, DOW_Close, DOW_Percent = getDowJonesDay()
	if NAS_Change >= 0:# If the NASDAQ was positive, then show in green.
		NAS_Color = drawGreen
	else:# Otherwise, show in red.
		NAS_Color = drawRed
	if DOW_Change >= 0:# If the Dow Jones was positive, then show in green.
		DOW_Color = drawGreen
	else:# Otherwise, show in red.
		DOW_Color = drawRed

	""" Create rec objects for the center buttons """
	button1Rect = pygame.Rect(buttonImage_rect.left, buttonImage_rect.top, SquareSize, SquareSize)
	button2Rect = pygame.Rect(buttonImage_rect.left+154, buttonImage_rect.top, SquareSize, SquareSize)
	button3Rect = pygame.Rect(buttonImage_rect.left+309, buttonImage_rect.top, SquareSize, SquareSize)
	button4Rect = pygame.Rect(buttonImage_rect.left, buttonImage_rect.bottom-126, SquareSize, SquareSize)
	button5Rect = pygame.Rect(buttonImage_rect.left+154, buttonImage_rect.bottom-126, SquareSize, SquareSize)
	button6Rect = pygame.Rect(buttonImage_rect.left+309, buttonImage_rect.bottom-126, SquareSize, SquareSize)
	
	tickersList = []
	while True:
		""" Detect mouse and keyboard events """
		for event in pygame.event.get():
			if event.type == QUIT: # Close the window.
				pygame.quit() # Quit the GUI.
				sys.exit() # Gracefully terminate the program.
			elif event.type == KEYDOWN: # Detect keypresses, adding them to the list representing the current ticker in the text input.
				if event.key == K_a:
					tickerList.append('A')
				if event.key == K_b:
					tickerList.append('B')
				if event.key == K_c:
					tickerList.append('C')
				if event.key == K_d:
					tickerList.append('D')
				if event.key == K_e:
					tickerList.append('E')
				if event.key == K_f:
					tickerList.append('F')
				if event.key == K_g:
					tickerList.append('G')
				if event.key == K_h:
					tickerList.append('H')
				if event.key == K_i:
					tickerList.append('I')
				if event.key == K_j:
					tickerList.append('J')
				if event.key == K_k:
					tickerList.append('K')
				if event.key == K_l:
					tickerList.append('L')
				if event.key == K_m:
					tickerList.append('M')
				if event.key == K_n:
					tickerList.append('N')
				if event.key == K_o:
					tickerList.append('O')
				if event.key == K_p:
					tickerList.append('P')
				if event.key == K_q:
					tickerList.append('Q')
				if event.key == K_r:
					tickerList.append('R')
				if event.key == K_s:
					tickerList.append('S')
				if event.key == K_t:
					tickerList.append('T')
				if event.key == K_u:
					tickerList.append('U')
				if event.key == K_v:
					tickerList.append('V')
				if event.key == K_w:
					tickerList.append('W')
				if event.key == K_x:
					tickerList.append('X')
				if event.key == K_y:
					tickerList.append('Y')
				if event.key == K_z:
					tickerList.append('Z')
				if event.key == K_6: #K_CARET
					tickerList.append('^')
				if event.key == K_BACKSPACE: # Simulate the action of the backspace in a text editor.
					try:
						tickerList.pop(-1)
					except IndexError: # Prevent errors if the tickerList is empty.
						Upper = False
				if event.key == K_KP1:# or K_1:
					tickerList.append('1')
				if event.key == K_KP_2:# or K_2:
					tickerList.append('2')
				if event.key == K_KP_3:# or K_3:
					tickerList.append('3')
				if event.key == K_KP_4:# or K_3:
					tickerList.append('4')
				if event.key == K_KP_5:# or K_3:
					tickerList.append('5')
				if event.key == K_KP_6:# or K_3:
					tickerList.append('6')
				if event.key == K_KP_7:# or K_3:
					tickerList.append('7')
				if event.key == K_KP_8:# or K_3:
					tickerList.append('8')
				if event.key == K_KP_9:# or K_3:
					tickerList.append('9')
				if event.key == K_KP_0:# or K_3:
					tickerList.append('0')
				if event.key == K_RETURN:
					if tickerList!=[] and "".join(tickerList) not in tickersList: # True if the text input is not empty or already in the ticker list.
						tickersList.append("".join(tickerList)) # Add the ticker to the ticker list.
					subprocess.Popen(['python', 'PystockGraphingForSubprocess.py', ">>".join(tickersList), Selected])# Launch another program to render the graphs of the desired stocks while making this program still functional at the same time.
					tickerList = [] # Reset the text input.
					tickersList = [] # Reset the ticker list.
			elif event.type == pygame.MOUSEBUTTONDOWN: # Detect mouse clicks within the window, handling them if they ought to interact with the program.
				mouse_pos = pygame.mouse.get_pos() # Get the mouse position in the window. 
				""" Time Range was clicked """
				if button1Rect.collidepoint(mouse_pos): # Select the 5 day time range.
					Selected = "5d"
				elif button2Rect.collidepoint(mouse_pos): # Select the 1 month time range.
					Selected = "1mo"
				elif button3Rect.collidepoint(mouse_pos): # Select the 6 month time range.
					Selected = "6mo"
				elif button4Rect.collidepoint(mouse_pos): # Select the 10 year time range.
					Selected = "10y"
				elif button5Rect.collidepoint(mouse_pos): # Select the Year To Date time range.
					Selected = "ytd"
				elif button6Rect.collidepoint(mouse_pos): # Select the Max time range.
					Selected = "max"
				""" Popular Stock Symbol was clicked """
				if DisneyRect.collidepoint(mouse_pos):
					tickerList = ['D', 'I', 'S']
				elif AppleRect.collidepoint(mouse_pos):
					tickerList = ['A', 'A', 'P', 'L']
				elif GoogleRect.collidepoint(mouse_pos):
					tickerList = ['G', 'O', 'O', 'G']
				elif AmazonRect.collidepoint(mouse_pos):
					tickerList = ['A', 'M', 'Z', 'N']
				elif FacebookRect.collidepoint(mouse_pos):
					tickerList = ['M', 'E', 'T', 'A']
				elif NetflixRect.collidepoint(mouse_pos):
					tickerList = ['N', 'F', 'L', 'X']
				""" Search Icon was clicked """
				if SearchRect.collidepoint(mouse_pos): # Clicked search icon.
					if tickerList!=[] and "".join(tickerList) not in tickersList: # True if the text input is not empty or already in the ticker list.
						tickersList.append("".join(tickerList)) # Add the ticker to the ticker list.
					subprocess.Popen(['python', 'PystockGraphingForSubprocess.py', ">>".join(tickersList), Selected]) # Launch another program to render the graphs of the desired stocks while making this program still functional at the same time.
					tickerList = [] # Reset the text input.
					tickersList = [] # Reset the ticker list.
				""" Add Ticker Icon was clicked """
				if AddRect.collidepoint(mouse_pos): # Clicked add ticker icon.
					if tickerList!=[] and "".join(tickerList) not in tickersList: # The new ticker is not already in the list of tickers.
						tickersList.append("".join(tickerList)) # Add it to the list of tickers.
					tickerList = [] # Clear the text input.
					
		if EvenOrOdd == 0: # Update the text input cursor emulator.
			EvenOrOdd = 1
		else:
			EvenOrOdd = 0
		
		""" Display the GUI """
		textTicker = "".join(tickerList) # Create the text of the current text input.
		windowSurface.fill(WHITE) # Reset the GUI.
		windowSurface.blit(pystockLogo, pystockLogo_rect) # Display the Pystock logo
		windowSurface.blit(buttonImage, buttonImage_rect)  # Display the center buttons.
		""" Display the Dow Jones and NASDAQ data from yesterday """
		windowSurface.blit(DOW_and_NAS, DOW_and_NAS_rect) # Display the image.
		NAS_Color(f"{round(NAS_Change, 2)} ({NAS_Percent}%)", font, windowSurface, Surface.right-120, 47) # Display a text representation of the data for the Dow Jones.
		DOW_Color(f"{round(DOW_Change, 2)} ({DOW_Percent}%)", font, windowSurface, Surface.right-120, 110) # Display a text representation of the data for the NASDAQ.
		""" Display the text input and cursor """
		if textTicker == "": # The text input is inactive.
			windowSurface.blit(textInputBoxBlank, TRect)
		else: # The text input is active.
			windowSurface.blit(textInputBoxActive, TRect)
			if EvenOrOdd == 0: # Draw the text input cursor emulator.
				drawText(textTicker, largeFont, windowSurface, Surface.centerx-100, Surface.bottom-57)
			else:
				drawText(f"{textTicker}|", largeFont, windowSurface, Surface.centerx-100, Surface.bottom-57)
		""" Display the selected graph type """
		if Selected == "max":
			drawText("Max of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		elif Selected == "ytd":
			drawText("YTD of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		elif Selected == "5d":
			drawText("5 days of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		elif Selected == "1mo":
			drawText("1 month of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		elif Selected == "6mo":
			drawText("6 months of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		elif Selected == "10y":
			drawText("10 years of:", font, windowSurface, Surface.centerx-100, Surface.bottom-97)
		if len(tickersList)>0: # True if the ticker list has at least one entered and another in the text box.
			windowSurface.blit(tickerListBox, tickerListBoxRect) # Display the ticker list box image.
			drawText("Plotlist:", largeFont, windowSurface, Surface.right-150, Surface.centery) # Display the list of different tickers in the tickerlist.
			for i in range(len(tickersList)):
				drawText(f"{tickersList[i]}", largeFont, windowSurface, Surface.right-150, Surface.centery+(50*(i+1)))
		""" Display the list of popular stocks """
		drawText("Popular", font, windowSurface, DisneyRect.left, DisneyRect.top-45) 
		drawText("Stocks", font, windowSurface, DisneyRect.left, DisneyRect.top-25)
		windowSurface.blit(Disney, DisneyRect)
		windowSurface.blit(Apple, AppleRect)
		windowSurface.blit(Google, GoogleRect)
		windowSurface.blit(Amazon, AmazonRect)
		windowSurface.blit(Facebook, FacebookRect)
		windowSurface.blit(Netflix, NetflixRect)
		windowSurface.blit(Search, SearchRect)
		windowSurface.blit(Add, AddRect)

		pygame.display.update() # Update the display window.
		mainClock.tick(4) # Delay the next update.

if __name__ == "__main__":
	# Run the project function.
	PYSTOCK()
