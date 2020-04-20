
#import images
import pgzrun
import random
import pygame

import sys
from pygame.locals import *

#constants
TITLE = 'Space Invaders: "A New Hope" Edition'


WIDTH = 250
HEIGHT = 500
SPEED = 5
ufo_speed = 9
ufostart = (random.randint(1,250))


#music
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(loops=-1)



#attributes for the game
class Game():
	def __init__(self):
		self.score = 0

game = Game()


#actors
#bad guys
ufo = Actor('tiefighter', (ufostart, 0))
ufo.y = ufo.height/2

ufo2 = Actor('tiefighter', (ufostart, 0))
ufo2.y = ufo2.height/2

bigufo = Actor('deethstarr', (ufostart, 0))

#blasts
pizza = Actor('laser', (-WIDTH, -HEIGHT))
pizza.active = False

quadcannonblast = Actor('morelaser', (-WIDTH, -HEIGHT))
quadcannonblast.active = False

#x-wing
rocketship = Actor('razorcrest', (WIDTH/2, HEIGHT))
rocketship.y = HEIGHT - rocketship.height/2


#define functions

#laser fires
def pizza_motion():
	if pizza.active == True:
		pizza.y -= SPEED
def fire():
	pizza.x = rocketship.x
	pizza.y = rocketship.y - rocketship.height/2 - pizza.height/2

def quad_motion():
	if quadcannonblast.active == True:
		quadcannonblast.y -= SPEED
def fire_quad():
	quadcannonblast.x = rocketship.x
	quadcannonblast.y = rocketship.y - rocketship.height/2 - quadcannonblast.height/2

#x-wing movmement
def get_keyboard(SPEED):
	if keyboard.left:
		rocketship.x -= SPEED
	elif keyboard.right:
		rocketship.x += SPEED
	elif keyboard.space:
		pizza.active = True
		fire()
	elif keyboard.down:
		quadcannonblast.active = True
		fire_quad()

def reset_ufo():
	ufo.y = 0
	ufo.x = random.randint(0 + ufo.width, WIDTH - ufo.width)

def reset_ufo2():
	ufo2.y = 0
	ufo2.x = random.randint(0 + ufo.width, WIDTH - ufo.width)

def rocketship_kill():
	rocketship.x = WIDTH/2

def ufo_get_past():
	if ufo.y == HEIGHT:
		reset_ufo()
		game.score -= 1
	elif ufo2.y == HEIGHT:
		reset_ufo2()
		game.score -= 1

def reset_pizza():
	pizza.pos = (-WIDTH, -HEIGHT)
	pizza.active = False

def reset_quad():
	quadcannonblast.pos = (-WIDTH, -HEIGHT)
	quadcannonblast.active = False

def out_screen():
	if rocketship.x > WIDTH:
		rocketship_kill()
		game.score -= 1

def test_hit():
	if ufo.colliderect(pizza):
		reset_ufo()
		reset_pizza()
		game.score += 1
	elif ufo2.colliderect(pizza):
		reset_ufo2()
		reset_pizza()
		game.score += 1
	elif ufo.colliderect(quadcannonblast):
		reset_ufo()
		reset_quad()
		game.score += 1
	elif ufo2.colliderect(quadcannonblast):
		reset_ufo2()
		reset_quad()
		game.score += 1

def ufo_motion():
	ufo.y += ufo_speed/3
	if ufo.y > HEIGHT:
		reset_ufo()
	ufo2.y += ufo_speed/3
	if ufo2.y > HEIGHT:
		reset_ufo2()

def deathstarmotion():
	bigufo.y += SPEED


#execute main functions
def update():
	get_keyboard(SPEED)
	ufo_motion()
	pizza_motion()
	test_hit()
	out_screen()
	ufo_get_past()
	deathstarmotion()
	quad_motion()

def draw():
	screen.clear()
	rocketship.draw()
	if game.score < 20:
		ufo.draw()
		ufo2.draw()
	pizza.draw()
	screen.draw.text(str(game.score), (WIDTH/20, HEIGHT/20))
	if game.score >= 20:
		bigufo.draw()
pgzrun.go()