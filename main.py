#import commands
import pgzrun
import random
import pygame
import os
import sys
import pygame.locals as pl
from pygame.locals import *
import pickle
import time
#from moveables import tie, tie2, tie3, ship, laser, quadcannonblast, protontorp, ion, game


#constants
WIDTH = 500
HEIGHT = 600
SPEED = 5
tie_speed = 9
tiestart = (random.randint(1,250))
BACKGROUND_IMAGE = 'background'
if len(sys.argv) >= 2:
    shipchoice = sys.argv[1]
else:
    shipchoice = 'xwing'

#shipchoice = sys.argv[1]

#music
# pygame.mixer.music.load('theme.mp3')
# pygame.mixer.music.play(loops=-1)

t1 = time.time()
print(t1)
#game attributes [score, level, ship, etc]
class Game():
    def __init__(self):
        self.level1quota = 150
        self.score = 0
        self.level = 1
        self.quaduse = 0
        self.tiesLet = 0
        self.tiesStopped = 0
        self.hitsHit = 0
        self.deaths = 0
        self.end = False
        #self.view = 'level-1'     #to test game mechanics - must be set to 'splash' in order for full functionality to be used
        self.view = 'splash'
        if len(sys.argv) >= 2:
            if sys.argv[1] == 'xwing':
                self.ship = shipchoice
            elif sys.argv[1] == 'falcon':
                self.ship = shipchoice
            elif sys.argv[1] == 'awing':
                self.ship = shipchoice
        else:
            self.ship = 'xwing'
game = Game()


def game_end():
    time.sleep(1)
    print(f'\n\nLevel 1 Complete!')
    print(f'\n\n\n\nFinal Stats:\n\nScore: {game.score}\nTies Hit: {game.hitsHit}\nDeaths: {game.deaths}\nTies Let Through: {game.tiesLet}')
    quit()

#actors
#tie fighters
tie = Actor('tiefighter', (tiestart, 0))
tie.y = tie.height/2
tie2 = Actor('tiefighter', (tiestart, 0))
tie2.y = tie2.height/2
tie3 = Actor('tiefighter', (tiestart, 0))
tie3.y = tie3.height/2
#standard laser, universal
laser = Actor('laser', (-WIDTH, -HEIGHT))
laser.active = False
#quad cannon blast, for the Millenium Falcon's ability
quadcannonblast = Actor('morelaser', (-WIDTH, -HEIGHT))
quadcannonblast.active = False
#ion blast, for the a=wing ability
ion = Actor('ion', (-WIDTH, -HEIGHT))
ion.active = False
#proton torpedo, for the x-wing ability
protontorp = Actor('torp', (-WIDTH, -HEIGHT))
protontorp.active = False
#x-wing
ship = Actor(game.ship, (WIDTH/2, HEIGHT))
ship.y = HEIGHT - ship.height/2


#set tie fighter speed
tie_speed == (game.score/300) + 9


#laser functions
def laser_motion():
    if laser.active == True:
        laser.y -= SPEED
def fire():
    laser.x = ship.x
    laser.y = ship.y - ship.height/2 - laser.height/2
#quad cannon functions
def quad_motion():
    if quadcannonblast.active == True:
        quadcannonblast.y -= SPEED
def fire_quad():
    quadcannonblast.x = ship.x
    quadcannonblast.y = ship.y - ship.height/2 - quadcannonblast.height/2
#ion blast functions
def ion_motion():
    if ion.active == True:
        ion.y -= SPEED
def fire_ion():
    ion.x = ship.x
    ion.y = ship.y - ship.height/2 - ion.height/2
#proton torpedo functions
def protontorp_motion():
    if protontorp.active == True:
        protontorp.y -= SPEED
def fire_protontorp():
    protontorp.x = ship.x
    protontorp.y = ship.y - ship.height/2 - protontorp.height/2


#movement and keyboard input
def get_keyboard(SPEED):
    if keyboard.left:
        ship.x -= SPEED
    elif keyboard.right:
        ship.x += SPEED
    elif keyboard.space:
        laser.active = True
        fire()
    elif keyboard.down:
        if game.view == 'splash':
            game.view = 'level-1'
        elif game.view == 'level-1':
            if game.ship == 'falcon':
                quadcannonblast.active = True
                fire_quad()
            elif game.ship == 'awing':
                ion.active = True
                fire_ion()
            elif game.ship == 'xwing':
                protontorp.active = True
                fire_protontorp()
            else:
                pass
        else:
            pass



#resets
#tie fighters
def reset_tie():
    tie.y = 0
    tie.x = random.randint(0 + tie.width, WIDTH - tie.width)
def reset_tie2():
    tie2.y = 0
    tie2.x = random.randint(0 + tie.width, WIDTH - tie.width)
def reset_tie3():
    tie3.y = 0
    tie3.x = random.randint(0 + tie.width, WIDTH - tie.width)
#player's ship
def ship_kill():
    ship.x = WIDTH/2
    game.score -= 100
    game.deaths += 1
    print(f'Deaths: {game.deaths}')
def out_screen():
    if ship.x > WIDTH:
        ship_kill()
        game.score -= 100
#weaponry
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


#check for hits
def test_hit():
    if tie.colliderect(laser):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser()
        game.score += addScore
        print(f'Tie 3 Killed with Laser. Added {addScore} points.')
        game.hitsHit += 1
    elif tie2.colliderect(laser):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser()
        game.score += add2Score
        print(f'Tie 2 Killed with Laser. Added {add2Score} points.')
        game.hitsHit += 1
    elif tie3.colliderect(laser):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser()
        game.score += add3Score
        print(f'Tie 3 Killed with Laser. Added {add3Score} points.')
        game.hitsHit += 1
    elif tie.colliderect(quadcannonblast):
        addQuadScore = round(100 + tie.x / 5)
        reset_tie()
        game.quaduse += 1
        game.score += addQuadScore
        print(f'Tie 1 Killed with Quad Blast. Added {addQuadScore} points.')
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
        game.hitsHit += 1
    elif tie2.colliderect(quadcannonblast):
        addQuad2Score = round(100 + tie2.x / 5)
        reset_tie2()
        game.quaduse += 1
        game.score += 100
        print(f'Tie 1 Killed with Quad Blast. Added {addQuad2Score} points.')
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
        game.hitsHit += 1
    elif tie3.colliderect(quadcannonblast):
        addQuad3Score = round(100 + tie3.x / 5)
        reset_tie3()
        game.quaduse += 1
        game.score += 100
        print(f'Tie 1 Killed with Quad Blast. Added {addQuad3Score} points.')
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
        game.hitsHit += 1
    elif tie.colliderect(ion):
        addIonScore = round(100 + ((tie3.x + tie2.x + tie.x) / 5))
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += addIonScore
        print(f'Tie 1 hit with Ion Blast. All Ties killed. Added {addIonScore} points.')
        game.hitsHit += 3
    elif tie2.colliderect(ion):
        addIon2Score = round(100 + ((tie3.x + tie2.x + tie.x) / 5))
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += addIon2Score
        print(f'Tie 2 hit with Ion Blast. All Ties killed. Added {addIon2Score} points.')
        game.hitsHit += 3
    elif tie3.colliderect(ion):
        addIon3Score = round(100 + ((tie3.x + tie2.x + tie.x) / 5))
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += addIon3Score
        print(f'Tie 3 hit with Ion Blast. All Ties killed. Added {addIon3Score} points.')
        game.hitsHit += 3
    elif tie.colliderect(protontorp):
        reset_tie()
        game.score += 100
        game.hitsHit += 1
    elif tie2.colliderect(protontorp):
        reset_tie2()
        game.score += 100
        game.hitsHit += 1
    elif tie3.colliderect(protontorp):
        reset_tie3()
        game.score += 100
        game.hitsHit += 1


def stopScoreFromZero():
    if game.score <= 0:
        game.score = 0
    else:
        pass

#motion
#tie fighters
def tie_motion():
    tie.y += tie_speed/3
    if tie.y > HEIGHT:
        reset_tie()
        game.score -= 200
        game.tiesLet += 1
    tie2.y += tie_speed/3
    if tie2.y > HEIGHT:
        reset_tie2()
        game.score -= 200
        game.tiesLet += 1
    tie3.y += tie_speed/3
    if tie3.y > HEIGHT:
        reset_tie3()
        game.score -= 200
        game.tiesLet += 1


#execute main functions
#update
def update():
    get_keyboard(SPEED)
    tie_motion()
    laser_motion()
    test_hit()
    out_screen()
    quad_motion()
    protontorp_motion()
    ion_motion()
    stopScoreFromZero()
    if game.level == 1:
        if game.level1quota <= game.hitsHit:
            game.end = True
    else:
        pass
    if game.end == True:
        game_end()
    else:
        pass
        
#draw
def draw():
    if game.view == 'level-1':
        screen.clear()
        screen.blit('background', (0,0))
        ship.draw()
        tie.draw()
        tie2.draw()
        tie3.draw()
        laser.draw()
        quadcannonblast.draw()
        ion.draw()
        protontorp.draw()
        screen.draw.text(str(f'Score: {game.score}'), (WIDTH/20, HEIGHT/20))
        screen.draw.text(str(f'Ties Killed: {game.hitsHit}'), (WIDTH/20, HEIGHT/30 - 5))
        screen.draw.text(str(f'Deaths: {game.deaths}'), (WIDTH/20, HEIGHT/10 - 15))
        screen.draw.text(str(f'Ties Escaped: {game.tiesLet}'), (WIDTH/20, HEIGHT/10))
    elif game.view == 'splash':
        screen.clear()
        screen.blit('logo', (0,0))
        screen.draw.text(str('<Press the DOWN key to begin>'), (WIDTH / 2, HEIGHT - 15))
    else:
        pass


#wrap up
pgzrun.go()

game_end()