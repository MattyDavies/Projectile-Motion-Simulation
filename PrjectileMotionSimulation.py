import pygame
from pygame.locals import *
import pygame_gui
import math
import numpy
import sys
import time


pygame.init()
running = False
menu = True


screenSize = (1900, 1000)
screen = pygame.display.set_mode(screenSize)
simSize = (math.floor(screenSize[0]*3/4), screenSize[1])
menuSize = (screenSize[0]-simSize[0], screenSize[0])
pygame.display.set_caption("Projectile Motion Simulation")
screen.fill((0,0,0))

#GUI Manager
manager = pygame_gui.UIManager(screenSize)
clock = pygame.time.Clock()

#Play btn
play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((simSize[0], 0), (100, 50)), text = "play/Stop", manager = manager)


#vars
g = ["g(m/s²)", -98]
psi = ["θ(ᵒ)", math.pi/3] #angle of release -> get usr input
v = ["u[m/s]", 300] #velocity -> get urs input

g_name = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0],50), (120, 50)), text = f"{g[0]}", manager = manager)
g_increase = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+120,50), (50, 50)), text = "↑", manager = manager)
g_decrease = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+170, 50), (50, 50)), text = "↓", manager = manager)
g_value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+220, 50), (100, 50)), text = f"{g[1]/10}", manager = manager)

psi_name = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0],100), (120, 50)), text = f"{psi[0]}", manager = manager)
psi_increase = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+120,100), (50, 50)), text = "↑", manager = manager)
psi_decrease = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+170, 100), (50, 50)), text = "↓", manager = manager)
psi_value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+220, 100), (100, 50)), text = f"{round(math.degrees(psi[1]))}", manager = manager)

v_name = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0],150), (120, 50)), text = f"{v[0]}", manager = manager)
v_increase = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+120,150), (50, 50)), text = "↑", manager = manager)
v_decrease = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+170, 150), (50, 50)), text = "↓", manager = manager)
v_value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0]+220, 150), (100, 50)), text = f"{v[1]/10}", manager = manager)

vel_arrow_color = [255,255,255,255]
grav_arrow_color = [255,255,255,255]

font = pygame.font.SysFont("timesnewroman", 20)