import pygame as pg
import sys
import random
import time
from game import *
from player import *
from monsters import *
from items import *




pg.init()
screen = pg.display.set_mode((800,457))
pg.display.set_caption("FileMania")
clock = pg.time.Clock()
game = Game(screen)
player = pg.sprite.GroupSingle()
player.add(Player())

monsters = pg.sprite.Group()

sheep_npc = Monsters("sheep")

monsters.add(sheep_npc)

items = pg.sprite.Group()




def collision_sprite():
    collided_monsters = pg.sprite.spritecollide(player.sprite, monsters, True)
    if collided_monsters:
        for monster in collided_monsters:
            if (monster.hasObject):
                monster.lastPosX = monster.rect.x
                monster.lastPosY = monster.rect.y
                monster.hasObject = False
                spawnItem(monster)

def spawnItem(monster):
    monster.Item = ChestPiece(monster.lastPosX, monster.lastPosY)
    items.add(monster.Item)
    


    # else:
    #     print("no collision")



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill('black')
    screen.blit(game.current_bg_ac, (0,0))
    player.draw(screen)
    player.update()

    monsters.draw(screen)
    monsters.update()

    collision_sprite()


    items.draw(screen)
    items.update()


    pg.display.update()
    clock.tick(60)


