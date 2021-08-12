'''
Hope for the Galaxy
A Game by Peter Nielsen (@peternielsen112)
This game is licensed under a GPL-3.0 License.
For How to Play, see the README.md file.
If you encounter a bug or have a suggestion, see README.md for instructions.
'''

# import statements
import pgzrun
import random
import pygame
import os
import sys
import pygame.locals as pl
from pygame.locals import *
import time


#constants
WIDTH = 585
HEIGHT = 700
SPEED = 5
tie_speed = 9
tiestart = (random.randint(1,250))
if len(sys.argv) >= 2:
    shipchoice = sys.argv[1]
else:
    shipchoice = 'xwing'

# music
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(loops=-1)

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
            elif sys.argv[1] == 'ywing':
                self.ship = shipchoice
            elif sys.argv[1] == 'razorcrest':
                self.ship = shipchoice
            elif sys.argv[1] == 'givemepowers':
                self.ship = 'deethstarr'
            else:
                self.ship = 'xwing'
        else:
            self.ship = 'xwing'
game = Game()

BACKGROUND_IMAGE = f'background{game.level}'

def game_end():
    time.sleep(1)
    t2 = time.time()
    t3 = t2-t1
    if game.end == True:
        print(f'\n\nLevel 1 Complete!')
    else:
        pass
    print(f'\n\n\n\nFinal Stats:\n\nScore: {game.score}\nTies Hit: {game.hitsHit}\nDeaths: {game.deaths}\nTies Let Through: {game.tiesLet}\nGame Total Time: {t3}')
    quit()

#actors
explosion = Actor('explosion', (-WIDTH, -HEIGHT))
explosion.inGame = False
explosion.times = 0
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
laser2 = Actor('laser', (-WIDTH, -HEIGHT))
laser2.active = False
laser3 = Actor('laser', (-WIDTH, -HEIGHT))
laser3.active = False
laser4 = Actor('laser', (-WIDTH, -HEIGHT))
laser4.active = False
laser5 = Actor('laser', (-WIDTH, -HEIGHT))
laser5.active = False
laser6 = Actor('laser', (-WIDTH, -HEIGHT))
laser6.active = False
laser7 = Actor('laser', (-WIDTH, -HEIGHT))
laser7.active = False
laser8 = Actor('laser', (-WIDTH, -HEIGHT))
laser8.active = False
laser9 = Actor('laser', (-WIDTH, -HEIGHT))
laser9.active = False
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

bomb = Actor('bomb', (-WIDTH,-HEIGHT))
bomb.active = False

#set tie fighter speed
tie_speed == (game.score/300) + 9


#laser functions
def laser_motion():
    if laser.active == True:
        laser.y -= SPEED
def fire():
    laser.x = ship.x
    laser.y = ship.y - ship.height/2 - laser.height/2
def laser2_motion():
    if laser2.active == True:
        laser2.y -= SPEED
def fire2():
    laser2.x = ship.x
    laser2.y = ship.y - ship.height/2 - laser2.height/2
def laser3_motion():
    if laser3.active == True:
        laser3.y -= SPEED
def fire3():
    laser3.x = ship.x
    laser3.y = ship.y - ship.height/2 - laser3.height/2
def laser4_motion():
    if laser4.active == True:
        laser4.y -= SPEED
def fire4():
    laser4.x = ship.x
    laser4.y = ship.y - ship.height/2 - laser4.height/2
def laser5_motion():
    if laser5.active == True:
        laser5.y -= SPEED
def fire5():
    laser5.x = ship.x
    laser5.y = ship.y - ship.height/2 - laser5.height/2
def laser6_motion():
    if laser6.active == True:
        laser6.y -= SPEED
def fire6():
    laser6.x = ship.x
    laser6.y = ship.y - ship.height/2 - laser6.height/2
def laser7_motion():
    if laser7.active == True:
        laser7.y -= SPEED
def fire7():
    laser7.x = ship.x
    laser7.y = ship.y - ship.height/2 - laser7.height/2
def laser8_motion():
    if laser8.active == True:
        laser8.y -= SPEED
def fire8():
    laser8.x = ship.x
    laser8.y = ship.y - ship.height/2 - laser8.height/2
def laser9_motion():
    if laser9.active == True:
        laser9.y -= SPEED
def fire9():
    laser9.x = ship.x
    laser9.y = ship.y - ship.height/2 - laser9.height/2
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
def bomb_motion():
    if bomb.active == True:
        bomb.y -= SPEED
def fire_bomb():
    bomb.x = ship.x
    bomb.y = ship.y-ship.height/2-protontorp.height/2


#movement and keyboard input
def get_keyboard(SPEED):
    if keyboard.left:
        ship.x -= SPEED
    elif keyboard.right:
        ship.x += SPEED
    elif keyboard.space:
        if laser.active == True:
            if laser2.active == True:
                if laser3.active == True:
                    if laser4.active == True:
                        if laser5.active == True:
                            if laser6.active == True:
                                if laser7.active  == True:
                                    if laser8.active == True:
                                        laser9.active = True
                                        fire9()
                                    else:
                                        laser8.active = True
                                        fire8()
                                else:
                                    laser7.active = True
                                    fire7()
                            else:
                                laser6.active = True
                                fire6()
                        else:
                            laser5.active = True
                            fire5()
                    else:
                        laser4.active = True
                        fire4()
                else:
                    laser3.active = True
                    fire3()
            else:
                laser2.active = True
                fire2()
        else:
            laser.active = True
            fire()
    elif keyboard.down:
        if game.view == 'splash':
            game.view = 'level-1'
            game.tiesLet = 0
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
            elif game.ship == 'ywing':
                bomb.active = True
                fire_bomb()
            else:
                pass
        else:
            pass



#resets
#tie fighters
def reset_tie():
    explosion.x = tie.x
    explosion.y = tie.y
    explosion.inGame = True
    tie.y = 0
    tie.x = random.randint(0, WIDTH)
def reset_tie2():
    explosion.x = tie2.x
    explosion.y = tie2.y
    explosion.inGame = True
    tie2.y = 0
    tie2.x = random.randint(0,WIDTH)
def reset_tie3():
    explosion.x = tie3.x
    explosion.y = tie3.y
    explosion.inGame = True
    tie3.y = 0
    tie3.x = random.randint(0,WIDTH)
#player's ship
def ship_kill():
    ship.x = WIDTH/2
    game.score -= 100
    game.deaths += 1
def out_screen():
    if ship.x > WIDTH:
        ship_kill()
        game.score -= 100
    elif ship.x < 0:
        ship_kill()
        game.score -= 100
    else:
        pass
#weaponry
def reset_laser():
    laser.pos = (-WIDTH, -HEIGHT)
    laser.active = False
def reset_laser2():
    laser2.pos = (-WIDTH, -HEIGHT)
    laser2.active = False
def reset_laser3():
    laser3.pos = (-WIDTH, -HEIGHT)
    laser3.active = False
def reset_laser4():
    laser4.pos = (-WIDTH, -HEIGHT)
    laser4.active = False
def reset_laser5():
    laser5.pos = (-WIDTH, -HEIGHT)
    laser5.active = False
def reset_laser6():
    laser6.pos = (-WIDTH, -HEIGHT)
    laser6.active = False
def reset_laser7():
    laser7.pos = (-WIDTH, -HEIGHT)
    laser7.active = False
def reset_laser8():
    laser8.pos = (-WIDTH, -HEIGHT)
    laser8.active = False
def reset_laser9():
    laser9.pos = (-WIDTH, -HEIGHT)
    laser9.active = False
def reset_quad():
    quadcannonblast.pos = (-WIDTH, -HEIGHT)
    quadcannonblast.active = False
def reset_ion():
    ion.pos = (-WIDTH, -HEIGHT)
    ion.active = False
def reset_torp():
    protontorp.pos = (-WIDTH, -HEIGHT)
    protontorp.active = False
def reset_bomb():
    bomb.pos = (-WIDTH, -HEIGHT)
    bomb.active = False


#check for hits
def test_hit():
    if tie.colliderect(laser):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser2):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser2()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser2):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser2()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser2):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser2()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser3):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser3()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser3):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser3()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser3):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser3()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser4):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser4()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser4):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser4()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser4):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser4()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser5):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser5()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser5):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser5()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser5):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser5()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser6):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser6()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser6):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser6()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser6):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser6()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser7):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser7()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser7):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser7()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser7):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser7()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser8):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser8()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser8):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser8()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser8):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser8()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(laser9):
        addScore = round(150 + tie.x / 5)
        reset_tie()
        reset_laser9()
        game.score += addScore
        game.hitsHit += 1
    elif tie2.colliderect(laser9):
        add2Score = round(150 + tie3.x / 5)
        reset_tie2()
        reset_laser9()
        game.score += add2Score
        game.hitsHit += 1
    elif tie3.colliderect(laser9):
        add3Score = round(150 + tie3.x / 5)
        reset_tie3()
        reset_laser9()
        game.score += add3Score
        game.hitsHit += 1
    elif tie.colliderect(quadcannonblast):
        addQuadScore = round(100 + tie.x / 5)
        reset_tie()
        game.quaduse += 1
        game.score += addQuadScore
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
        game.hitsHit += 1
    elif tie2.colliderect(quadcannonblast):
        addQuad2Score = round(100 + tie2.x / 5)
        reset_tie2()
        game.quaduse += 1
        game.score += 100
        if game.quaduse == 2:
            reset_quad()
            game.quaduse -= 2
        game.hitsHit += 1
    elif tie3.colliderect(quadcannonblast):
        addQuad3Score = round(100 + tie3.x / 5)
        reset_tie3()
        game.quaduse += 1
        game.score += 100
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
        game.hitsHit += 3
    elif tie2.colliderect(ion):
        addIon2Score = round(100 + ((tie3.x + tie2.x + tie.x) / 5))
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += addIon2Score
        game.hitsHit += 3
    elif tie3.colliderect(ion):
        addIon3Score = round(100 + ((tie3.x + tie2.x + tie.x) / 5))
        reset_tie()
        reset_tie2()
        reset_tie3()
        game.score += addIon3Score
        game.hitsHit += 3
    elif tie.colliderect(protontorp):
        addProtonScore = round(100 + tie.x / 5)
        reset_tie()
        game.score += addProtonScore
        game.hitsHit += 1
    elif tie2.colliderect(protontorp):
        addProton2Score = round(100 + tie2.x / 5)
        reset_tie2()
        game.score += addProton2Score
        game.hitsHit += 1
    elif tie3.colliderect(protontorp):
        addProton3Score = round(100 + tie3.x / 5)
        reset_tie3()
        game.score += addProton3Score
        game.hitsHit += 1
    elif tie.colliderect(bomb):
        addBombScore = round(100 + tie.x/5)
        reset_tie()
        reset_bomb()
        game.score += addBombScore
        game.hitsHit += 1
    elif tie2.colliderect(bomb):
        addBomb2Score = round(100 + tie2.x/5)
        reset_tie2()
        reset_bomb()
        game.score += addBomb2Score
        game.hitsHit += 1
    elif tie3.colliderect(bomb):
        addBomb3Score = round(100 + tie3.x/5)
        reset_tie3()
        reset_bomb()
        game.score += addBomb3Score
        game.hitsHit += 1
    elif tie.colliderect(ship):
        if len(sys.argv) > 2:
            if sys.argv[1] == 'givemepowers':
                reset_tie()
            else:
                reset_tie()
                ship_kill()
        else:
            reset_tie()
            ship_kill()
    elif tie2.colliderect(ship):
        if len(sys.argv) > 2:
            if sys.argv[1] == 'givemepowers':
                reset_tie2()
            else:
                reset_tie2()
                ship_kill()
        else:
            reset_tie2()
            ship_kill()
    elif tie3.colliderect(ship):
        if len(sys.argv) > 2:
            if sys.argv[1] == 'givemepowers':
                reset_tie3()
            else:
                reset_tie3()
                ship_kill()
        else:
            reset_tie3()
            ship_kill()
    else:
        pass



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
    laser2_motion()
    laser3_motion()
    laser4_motion()
    laser5_motion()
    laser6_motion()
    laser7_motion()
    laser8_motion()
    laser9_motion()
    test_hit()
    out_screen()
    quad_motion()
    protontorp_motion()
    ion_motion()
    bomb_motion()
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
    if explosion.inGame == True:
        explosion.times += 1
    else:
        pass
    if explosion.times >= 15:
        explosion.times = 0
        explosion.inGame = False
        explosion.x = -WIDTH
        explosion.y = -HEIGHT
    else:
        pass
    if laser.y < 0:
        laser.active = False
    else:
        pass
    if laser2.y < 0:
        laser2.active = False
    else:
        pass
    if laser3.y < 0:
        laser3.active = False
    else:
        pass
    if laser4.y < 0:
        laser4.active = False
    else:
        pass
    if laser5.y < 0:
        laser5.active = False
    else:
        pass
    if laser6.y < 0:
        laser6.active = False
    else:
        pass
    if laser7.y < 0:
        laser7.active = False
    else:
        pass
    if laser8.y < 0:
        laser8.active = False
    else:
        pass
    if laser9.y < 0:
        laser9.active = False
    else:
        pass
        
        
#draw
def draw():
    if game.view == 'level-1':
        screen.clear()
        screen.blit(BACKGROUND_IMAGE, (0,0))
        explosion.draw()
        ship.draw()
        tie.draw()
        tie2.draw()
        tie3.draw()
        laser.draw()
        laser2.draw()
        laser3.draw()
        laser4.draw()
        laser5.draw()
        laser6.draw()
        laser7.draw()
        laser8.draw()
        laser9.draw()
        quadcannonblast.draw()
        ion.draw()
        protontorp.draw()
        bomb.draw()
        screen.draw.text(str(f'Score: {game.score}'), (WIDTH/20, HEIGHT/20))
        screen.draw.text(str(f'Ties Killed: {game.hitsHit}'), (WIDTH/20, HEIGHT/30 - 5))
        screen.draw.text(str(f'Deaths: {game.deaths}'), (WIDTH/20, HEIGHT/10 - 15))
        screen.draw.text(str(f'Ties Escaped: {game.tiesLet}'), (WIDTH/20, HEIGHT/10))
    elif game.view == 'splash':
        screen.clear()
        screen.blit('logo', (WIDTH * 0.08,HEIGHT/3))
        screen.draw.text(str('<Press the DOWN key to begin>'), (WIDTH - 400, HEIGHT - 30))
    else:
        pass


#wrap up
pgzrun.go()

game_end()