"""
Name: AaronTook
Use:  A Stock Market GUI using Pygame and the YFinance modules (along with others, see requirements.txt for details)
"""

# Set up the window and hide the message.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Standard imports.
import pygame, sys, time, random, subprocess
from pygame.locals import *
# Custom imports.
from Financing import *


# Set up the pygame.
pygame.init()

# Set up the colors.
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (34,177,76)

# Set up the basic functions.
def drawText(text,font,surface,x,y,COLOR=BLACK):
	textobj = font.render(text,1,COLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj, textrect)

def drawRed(text,font,surface,x,y):
	textobj = font.render(text,1,RED)
	textrect = textobj.get_rect()
	textrect.topright = (x,y)
	surface.blit(textobj, textrect)

def drawGreen(text,font,surface,x,y):
	textobj = font.render(text,1,GREEN)
	textrect = textobj.get_rect()
	textrect.topright = (x,y)
	surface.blit(textobj, textrect)

def drawChoice(text,font,surface,x,y):
	textobj = font.render(text,1,BLACK)
	textrect = textobj.get_rect()
	textrect.center = (x,y)
	surface.blit(textobj, textrect)

def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				return

def Im(ImageName):
	return pygame.image.load(f'images/{ImageName}.png')

def Spr(ImageName):
	return pygame.image.load(f'images/{ImageName}.png'), pygame.image.load(f'images/{ImageName}.png').get_rect()

# The main function
def PYSTOCK():
	# Set up the fonts, sizes, and the basic window and pygame operators.
	WINDOWWIDTH = 1000
	WINDOWHEIGHT = 700
	CityFont = pygame.font.SysFont(None, 50)
	font = pygame.font.SysFont(None, 22)
	score_font = pygame.font.SysFont(None,32)
	windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('PyStock')
	mainClock = pygame.time.Clock()
	Surface = pygame.Rect(0,0,WINDOWWIDTH,WINDOWHEIGHT)
	
	# Define the Spr objects (images and their Rects).
	PSL,PSL_rect = Spr("PystockLogo1")
	Pystock_icon = pygame.transform.scale(pygame.image.load("images/Blank.png"), (32,32))
	pygame.display.set_icon(Pystock_icon)
	PCHART,PCHART_rect = Spr("PystockChoices")
	DOW_and_NAS, DOW_and_NAS_rect = Spr("DowAndNasdaq")
	TickerWithMessage,TRect = Spr("Ticker_with_message")
	TickerNoMessage,TRect = Spr("Ticker_blank")
	TRect.midbottom = Surface.midbottom
	TRect.bottom-=15
	PCHART_rect.center = Surface.center
	PCHART_rect.centery+=30
	PSL_rect.centerx = Surface.centerx
	DOW_and_NAS_rect.right = Surface.right
	Search,SearchRect = Spr("Search")
	SearchRect.centery = TRect.centery
	SearchRect.left = TRect.right+25
	Add,AddRect = Spr("AddTicker")
	AddRect.topleft = SearchRect.topright
	AddRect.left += 25
	Box2,Box2Rect = Spr("Box2")
	Box2Rect.topleft = (Surface.right-165,Surface.centery-15)
	
	Disney,DisneyRect = Spr("Disney")
	Apple,AppleRect = Spr("Apple")
	Google,GoogleRect = Spr("Google")
	Amazon,AmazonRect = Spr("Amazon")
	Facebook,FacebookRect = Spr("Facebook")
	Netflix,NetflixRect = Spr("Netflix")
	DisneyRect.top = PSL_rect.bottom
	AppleRect.top = DisneyRect.bottom+25
	GoogleRect.top = AppleRect.bottom+25
	AmazonRect.top = GoogleRect.bottom+25
	FacebookRect.top = AmazonRect.bottom+25
	NetflixRect.top = FacebookRect.bottom+25
	DisneyRect.left = 25
	AppleRect.left = 25
	GoogleRect.left = 25
	AmazonRect.left = 25
	FacebookRect.left = 25
	NetflixRect.left = 25
	
	# Define random variables.
	SquareSize = 126
	Selected = "max"
	Message = ""
	Username = []
	EvenOrOdd = 1
	TYPING = False
	
	# Get the stock data.
	NAS_Change,NAS_Close,NAS_Percent = getNASDAQDay()
	DOW_Change,DOW_Close,DOW_Percent = getDowJonesDay()
	if NAS_Change >= 0:# If the NASDAQ was positive, then show green.
		NAS_Color = drawGreen
	else:# Otherwise, show red.
		NAS_Color = drawRed
	if DOW_Change >= 0:# If the Dow Jones was positive, then show green.
		DOW_Color = drawGreen
	else:# Otherwise, show red.
		DOW_Color = drawRed
	
	B1Rect = pygame.Rect(PCHART_rect.left,PCHART_rect.top,SquareSize,SquareSize)
	B2Rect = pygame.Rect(PCHART_rect.left+154,PCHART_rect.top,SquareSize,SquareSize)
	B3Rect = pygame.Rect(PCHART_rect.left+309,PCHART_rect.top,SquareSize,SquareSize)
	B4Rect = pygame.Rect(PCHART_rect.left,PCHART_rect.bottom-126,SquareSize,SquareSize)
	B5Rect = pygame.Rect(PCHART_rect.left+154,PCHART_rect.bottom-126,SquareSize,SquareSize)
	B6Rect = pygame.Rect(PCHART_rect.left+309,PCHART_rect.bottom-126,SquareSize,SquareSize)
	
	TickersList = []
	while True:
		# This is a keypress detection system. 
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_a:
					Username.append('A')
				if event.key == K_b:
					Username.append('B')
				if event.key == K_c:
					Username.append('C')
				if event.key == K_d:
					Username.append('D')
				if event.key == K_e:
					Username.append('E')
				if event.key == K_f:
					Username.append('F')
				if event.key == K_g:
					Username.append('G')
				if event.key == K_h:
					Username.append('H')
				if event.key == K_i:
					Username.append('I')
				if event.key == K_j:
					Username.append('J')
				if event.key == K_k:
					Username.append('K')
				if event.key == K_l:
					Username.append('L')
				if event.key == K_m:
					Username.append('M')
				if event.key == K_n:
					Username.append('N')
				if event.key == K_o:
					Username.append('O')
				if event.key == K_p:
					Username.append('P')
				if event.key == K_q:
					Username.append('Q')
				if event.key == K_r:
					Username.append('R')
				if event.key == K_s:
					Username.append('S')
				if event.key == K_t:
					Username.append('T')
				if event.key == K_u:
					Username.append('U')
				if event.key == K_v:
					Username.append('V')
				if event.key == K_w:
					Username.append('W')
				if event.key == K_x:
					Username.append('X')
				if event.key == K_y:
					Username.append('Y')
				if event.key == K_z:
					Username.append('Z')
				if event.key == K_BACKSPACE:
					try:
						Username.pop(-1)
					except IndexError:
						Upper = False
				if event.key == K_KP1:# or K_1:
					Username.append('1')
				if event.key == K_KP_2:# or K_2:
					Username.append('2')
				if event.key == K_KP_3:# or K_3:
					Username.append('3')
				if event.key == K_KP_4:# or K_3:
					Username.append('4')
				if event.key == K_KP_5:# or K_3:
					Username.append('5')
				if event.key == K_KP_6:# or K_3:
					Username.append('6')
				if event.key == K_KP_7:# or K_3:
					Username.append('7')
				if event.key == K_KP_8:# or K_3:
					Username.append('8')
				if event.key == K_KP_9:# or K_3:
					Username.append('9')
				if event.key == K_KP_0:# or K_3:
					Username.append('0')
				if event.key == K_RETURN:
					if Username!=[] and "".join(Username) not in TickersList:
						TickersList.append("".join(Username))
					# Launch another program to render the graphs of the desired stocks while making this program still functional at the same time.
					subprocess.Popen(['python', 'PystockGraphingForSubprocess.py',">>".join(TickersList),Selected])
					Username = []
					TickersList = []
					
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if B1Rect.collidepoint(mouse_pos):
					Selected = "5d"
				elif B2Rect.collidepoint(mouse_pos):
					Selected = "1mo"
				elif B3Rect.collidepoint(mouse_pos):
					Selected = "6mo"
				elif B4Rect.collidepoint(mouse_pos):
					Selected = "10y"
				elif B5Rect.collidepoint(mouse_pos):
					Selected = "ytd"
				elif B6Rect.collidepoint(mouse_pos):
					Selected = "max"
				elif DisneyRect.collidepoint(mouse_pos):
					Username = ['D','I','S']
				elif AppleRect.collidepoint(mouse_pos):
					Username = ['A','A','P','L']
				elif GoogleRect.collidepoint(mouse_pos):
					Username = ['G','O','O','G']
				elif AmazonRect.collidepoint(mouse_pos):
					Username = ['A','M','Z','N']
				elif FacebookRect.collidepoint(mouse_pos):
					Username = ['F','B']
				elif NetflixRect.collidepoint(mouse_pos):
					Username = ['N','F','L','X']
				elif SearchRect.collidepoint(mouse_pos):
					if Username!=[] and "".join(Username) not in TickersList:
						TickersList.append("".join(Username))
					# Launch another program to render the graphs of the desired stocks while making this program still functional at the same time.
					subprocess.Popen(['python', 'PystockGraphingForSubprocess.py',">>".join(TickersList),Selected])
					Username = []
					TickersList = []
				elif AddRect.collidepoint(mouse_pos):
					if Username!=[] and "".join(Username) not in TickersList:
						TickersList.append("".join(Username))
					Username = []
					
		if EvenOrOdd == 0:
			EvenOrOdd = 1
		else:
			EvenOrOdd = 0
		
		# Display the GUI
		Message = "".join(Username)
		windowSurface.fill(WHITE)
		windowSurface.blit(PSL,PSL_rect)
		windowSurface.blit(PCHART,PCHART_rect)
		windowSurface.blit(DOW_and_NAS,DOW_and_NAS_rect)
		NAS_Color(f"{round(NAS_Change,2)} ({NAS_Percent}%)",font,windowSurface,Surface.right-10,47)
		DOW_Color(f"{round(DOW_Change,2)} ({DOW_Percent}%)",font,windowSurface,Surface.right-10,110)
		if Message == "":
			windowSurface.blit(TickerWithMessage,TRect)
		else:
			windowSurface.blit(TickerNoMessage,TRect)
			if EvenOrOdd == 0:
				drawText(Message,CityFont,windowSurface,Surface.centerx-100,Surface.bottom-57)
			else:
				drawText(f"{Message}|",CityFont,windowSurface,Surface.centerx-100,Surface.bottom-57)
		if Selected == "max":
			drawText("Max of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		elif Selected == "ytd":
			drawText("YTD of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		elif Selected == "5d":
			drawText("5 days of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		elif Selected == "1mo":
			drawText("1 month of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		elif Selected == "6mo":
			drawText("6 months of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		elif Selected == "10y":
			drawText("10 years of:",font,windowSurface,Surface.centerx-100,Surface.bottom-97)
		if len(TickersList)>0:
			windowSurface.blit(Box2,Box2Rect)
			drawText("Plotlist:",CityFont,windowSurface,Surface.right-150,Surface.centery)
			for i in range(len(TickersList)):
				drawText(f"{TickersList[i]}",CityFont,windowSurface,Surface.right-150,Surface.centery+(50*(i+1)))
		
		drawText("Popular",font,windowSurface,DisneyRect.left,DisneyRect.top-45)
		drawText("Stocks",font,windowSurface,DisneyRect.left,DisneyRect.top-25)
		windowSurface.blit(Disney,DisneyRect)
		windowSurface.blit(Apple,AppleRect)
		windowSurface.blit(Google,GoogleRect)
		windowSurface.blit(Amazon,AmazonRect)
		windowSurface.blit(Facebook,FacebookRect)
		windowSurface.blit(Netflix,NetflixRect)
		windowSurface.blit(Search,SearchRect)
		windowSurface.blit(Add,AddRect)

		pygame.display.update()
		mainClock.tick(4)

if __name__ == "__main__":
	PYSTOCK()
