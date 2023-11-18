import pygame as pg
import sys
import random
import time
from game import *
from player import *




pg.init()
screen = pg.display.set_mode((800,457))
pg.display.set_caption("FileMania")
clock = pg.time.Clock()
game = Game(screen)
player = pg.sprite.GroupSingle()
player.add(Player())




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill('black')
    screen.blit(game.current_bg, (0,0))
    player.draw(screen)
    player.update()

    pg.display.update()
    clock.tick(60)


