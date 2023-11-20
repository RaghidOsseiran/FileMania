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

#Player group and instance
player = pg.sprite.GroupSingle()
player.add(Player())

#Monster group and instance
monsters = pg.sprite.Group()
sheep_npc = Monsters("sheep")
monsters.add(sheep_npc)

#Items group
items = pg.sprite.Group()

items_font = pg.font.Font("images/font/Pixeltype.ttf", 20)



def collision_sprite():
    collided_monsters = pg.sprite.spritecollide(player.sprite, monsters, True)
    if collided_monsters:
        for monster in collided_monsters:
            if (monster.hasObject):
                monster.lastPosX = monster.rect.x
                monster.lastPosY = monster.rect.y
                monster.hasObject = False
                spawnItem(monster)


def draw_text(text, color, surface, x, y):
    text_surface = items_font.render(text, False, color)
    text_rect = text_surface.get_rect(topleft = (x, y-25))
    surface.blit(text_surface, text_rect)



def collision_item():
    collided_items = pg.sprite.spritecollide(player.sprite, items, False)
    if collided_items:
        for item in collided_items:
            collide_message = "Press E to pick up item"
            draw_text(collide_message, "white", screen, item.rect.x, item.rect.y)
    return collided_items
            


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

    collided_items = collision_item()
    keys = pg.key.get_pressed()
    if keys[pg.K_e]:
        for item in collided_items:
            print("pressing E")
            items.remove(item)


    pg.display.update()
    clock.tick(60)


