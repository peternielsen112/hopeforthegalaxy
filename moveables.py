import pgzrun
import random
import pygame
import os
import sys
import pygame.locals as pl
from pygame.locals import *
import pgzero


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
