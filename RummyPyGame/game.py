import pygame
import sys
import random

pygame.init()
gamedeck=[]
p1deck=[]
p2deck=[]

v=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
s=["C","D","H","S"]

def makeDeck():
	for i in range(len(v)):
		for j in range(len(s)):
			gamedeck.append(v[i]+s[j])
	return gamedeck

def drawCard(deck):
	x=random.randint(0,len(deck)-1)
	a=deck.pop(x)
	return a

def dist():
	for i in range(13):
		p1deck.append(drawCard(gamedeck))
		p2deck.append(drawCard(gamedeck))

makeDeck()
dist()
stock=gamedeck

screenSize=width,height=1065,600
screen=pygame.display.set_mode(screenSize)
back=pygame.image.load("2.jpg")
back=pygame.transform.scale(back,screenSize)
screen.blit(back,(0,0))

cardSize=(60,80)

cardback=pygame.transform.scale(pygame.image.load("cards/back.png"),cardSize)
stockCard=drawCard(stock)
stockCardx=pygame.transform.scale(pygame.image.load("cards/"+stockCard+".png"),cardSize)
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			sys.exit()
		if(event.type==pygame.MOUSEBUTTONDOWN):
			pygame.display.flip()
			backGame=pygame.image.load("1.jpg")
			backGame=pygame.transform.scale(backGame,screenSize)
			screen.blit(backGame,(0,0))
			screen.blit(cardback,(250,120))
			screen.blit(stockCardx,(320,120))
			for i in range(len(p1deck)):
				pygame.display.flip()
				x=pygame.transform.scale(pygame.image.load("cards/"+p1deck[i]+".png"),cardSize)
				screen.blit(x,(50+(70*i),300))
		



		






