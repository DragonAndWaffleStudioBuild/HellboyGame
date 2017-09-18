#!/usr/bin/python
#coding: latin-1

import pygame
pygame.init()

from random import randint as ran

w,h = 700,700
w1,h1 = w/20,h/20
gameDisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption('Warcraft')

green = (0,155,0)
red = (255,0,0)
silver=(179, 179, 179)
white = (255,255,255)
cyan = (11,99,250)
gold = (253,159,29)
black=(0,0,0)

block_type = {"grass":[pygame.image.load('images/grass.png'),1]}

clock = pygame.time.Clock()
fps=10

smallfont = pygame.font.Font("fonts/fish.TTF", 10)
medfont = pygame.font.Font("fonts/fish.TTF", 30)
largefont = pygame.font.Font("fonts/fish.TTF", 80)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)   
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,a, size,y_displace=0):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (a[0]), (a[1])+y_displace
    gameDisplay.blit(textSurf, textRect)

def start():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(black)
		message_to_screen("A DragonAndWaffleStudio",red,[w/2,h/2-30],"medium")
		message_to_screen("Production!!!",red,[w/2,h/2],"medium")
		message_to_screen("COPYRIGHT DragonAndWaffleStudio 2017",red,[w/2,h-20],"small")
		message_to_screen("",red,[w/2,h-20],"small")
		pygame.display.update()
		clock.tick(fps)

start()
pygame.quit()
