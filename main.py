#import images
import pgzrun
import random
import pygame
import os
import sys
import pygame.locals as pl
from pygame.locals import *


#falcon
#awing
#xwing
#razorcrest


#constants
TITLE = 'Space Invaders: "A New Hope" Edition'


WIDTH = 384
HEIGHT = 683
SPEED = 5
tie_speed = 9
tiestart = (random.randint(1,250))
BACKGROUND_IMAGE = 'background'

#music
pygame.mixer.music.load('theme.mp3')
#pygame.mixer.music.play(loops=-1)

#attributes for the game
class Game():
    def __init__(self):
        self.score = 0
        self.level = 1
        self.quaduse = 0
        self.view = 'splash'
        if sys.argv[1] == 'xwing':
            self.ship = sys.argv[1]
        elif sys.argv[1] == 'falcon':
            self.ship = sys.argv[1]
        elif sys.argv[1] == 'awing':
            self.ship = sys.argv[1]
        else:
            self.ship = 'xwing'
#specify ship can be 'falcon', 'awing', 'razorcrest', or 'xwing'
game = Game()



#actors
#bad guys
tie = Actor('tiefighter', (tiestart, 0))
tie.y = tie.height/2

tie2 = Actor('tiefighter', (tiestart, 0))
tie2.y = tie2.height/2

tie3 = Actor('tiefighter', (tiestart, 0))
tie3.y = tie3.height/2

bigtie = Actor('deethstarr', (tiestart, 0))

#blasts
laser = Actor('laser', (-WIDTH, -HEIGHT))
laser.active = False

quadcannonblast = Actor('morelaser', (-WIDTH, -HEIGHT))
quadcannonblast.active = False

ion = Actor('ion', (-WIDTH, -HEIGHT))
ion.active = False

protontorp = Actor('torp', (-WIDTH, -HEIGHT))
protontorp.active = False

#x-wing
ship = Actor(game.ship, (WIDTH/2, HEIGHT))
ship.y = HEIGHT - ship.height/2


#define functions


tie_speed == (game.score/300) + 9


#laser fires
def laser_motion():
    if laser.active == True:
        laser.y -= SPEED
def fire():
    laser.x = ship.x
    laser.y = ship.y - ship.height/2 - laser.height/2

def quad_motion():
    if quadcannonblast.active == True:
        quadcannonblast.y -= SPEED
def fire_quad():
    quadcannonblast.x = ship.x
    quadcannonblast.y = ship.y - ship.height/2 - quadcannonblast.height/2
def ion_motion():
    if ion.active == True:
        ion.y -= SPEED
def fire_ion():
    ion.x = ship.x
    ion.y = ship.y - ship.height/2 - ion.height/2
def protontorp_motion():
    if protontorp.active == True:
        protontorp.y -= SPEED
def fire_protontorp():
    protontorp.x = ship.x
    protontorp.y = ship.y - ship.height/2 - protontorp.height/2

#x-wing movmement
def get_keyboard(SPEED):
    if keyboard.left:
        ship.x -= SPEED
    elif keyboard.right:
        ship.x += SPEED
    elif keyboard.space:
        laser.active = True
        fire()
    if game.ship == 'falcon':
        if keyboard.down:
            quadcannonblast.active = True
            fire_quad()
    elif game.ship == 'awing':
        if keyboard.down:
            ion.active = True
            fire_ion()
    elif game.ship == 'xwing':
        if keyboard.down:
            protontorp.active = True
            fire_protontorp()
def reset_tie():
    tie.y = 0
    tie.x = random.randint(0 + tie.width, WIDTH - tie.width)

def reset_tie2():
    tie2.y = 0
    tie2.x = random.randint(0 + tie.width, WIDTH - tie.width)

def reset_tie3():
    tie3.y = 0
    tie3.x = random.randint(0 + tie.width, WIDTH - tie.width)

def ship_kill():
    ship.x = WIDTH/2
    game.score -= 100


def reset_laser():
    laser.pos = (-WIDTH, -HEIGHT)
    laser.active = False

def reset_quad():
    quadcannonblast.pos = (-WIDTH, -HEIGHT)
    quadcannonblast.active = False

def reset_ion():
    ion.pos = (-WIDTH, -HEIGHT)
    ion.active = False

def reset_torp():
    protontorp.pos = (-WIDTH, -HEIGHT)
    protontorp.active = False

def out_screen():
    if ship.x > WIDTH:
        ship_kill()
        game.score -= 100

def test_hit():
    if tie.colliderect(laser):
        reset_tie()
        reset_laser()
        game.score += 100
    elif tie2.colliderect(laser):
        reset_tie2()
        reset_laser()
        game.score += 100
    elif tie3.colliderect(laser):
        reset_tie3()
        reset_laser()
        game.score += 100
    elif tie.colliderect(quadcannonblast):
        reset_tie()
        game.quaduse += 1
        game.score += 250
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2

    elif tie2.colliderect(quadcannonblast):
        reset_tie2()
        game.quaduse += 1
        game.score += 250
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2

    elif tie3.colliderect(quadcannonblast):
        reset_tie3()
        game.quaduse += 1
        game.score += 250
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
    elif tie.colliderect(ion):
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += 1000
    elif tie.colliderect(protontorp):
        reset_tie()
        game.score += 100
    elif tie2.colliderect(protontorp):
        reset_tie2()
        game.score += 100
    elif tie3.colliderect(protontorp):
        reset_tie3()
        game.score += 100




def tie_motion():
    tie.y += tie_speed/3
    if tie.y > HEIGHT:
        reset_tie()
        game.score -= 200
    tie2.y += tie_speed/3
    if tie2.y > HEIGHT:
        reset_tie2()
        game.score -= 200
    tie3.y += tie_speed/3
    if tie3.y > HEIGHT:
        reset_tie3()
        game.score -= 200

def deathstarmotion():
    bigtie.y += SPEED
    if bigtie.y > HEIGHT:
        pass


#execute main functions
def update():
    get_keyboard(SPEED)
    tie_motion()
    laser_motion()
    test_hit()
    out_screen()
    deathstarmotion()
    quad_motion()
    protontorp_motion()
    ion_motion()

def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMAGE, (0,0))
    ship.draw()
    tie.draw()
    tie2.draw()
    tie3.draw()
#	if game.score < 20:
#		tie.draw()
#		tie2.draw()
    laser.draw()
    quadcannonblast.draw()
    ion.draw()
    protontorp.draw()
    screen.draw.text(str(game.score), (WIDTH/20, HEIGHT/20))
#	if game.score >= 20:
#		bigtie.draw()
pgzrun.go()
