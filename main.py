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
player_instance = Player()
player.add(player_instance)

#Monster group and instance
monsters = pg.sprite.Group()
sheep_npc = Sheep(585, 438)
monsters.add(sheep_npc)


npcs = pg.sprite.Group()
SpawnKeeper_npc = SpawnKeeper(35,438)
npcs.add(SpawnKeeper_npc)



#Items group
items = pg.sprite.Group()

items_font = pg.font.Font("images/font/Pixeltype.ttf", 20)




def draw_text(text, color, surface, x, y):
    text_surface = items_font.render(text, False, color)
    text_rect = text_surface.get_rect(topleft = (x, y-25))
    surface.blit(text_surface, text_rect)

def get_sprites_in_group(group):
    return group.sprites()


# collsision functions

def collision_sprite_monsters():
    collided_monsters = pg.sprite.spritecollide(player.sprite, monsters, True)
    if collided_monsters:
        for monster in collided_monsters:
            if (monster.hasObject and monster.type == "sheep"):
                print("sheep if")
                monster.lastPosX = monster.rect.x
                monster.lastPosY = monster.rect.y
                monster.hasObject = False
                spawnItem(monster)


def spawnItem(monster):
    monster.Item = ChestPiece(monster.lastPosX, monster.lastPosY)
    items.add(monster.Item)
                    


def collision_item():
    collided_items = pg.sprite.spritecollide(player.sprite, items, False)
    if collided_items:
        for item in collided_items:
            collide_message = "Press E to pick up item"
            draw_text(collide_message, "white", screen, item.rect.x, item.rect.y)
    return collided_items


def collision_sprite_npcs():
    collided_npcs = pg.sprite.spritecollide(player.sprite, npcs, False)
    if collided_npcs:
        for npc in collided_npcs:
            if (npc.hasObject and npc.type == "spawnkeeper"):
                # i want to add the option to press E to talk
                keys = pg.key.get_pressed()
                if keys[pg.K_e]:
                    interactions_sprite_npcs(npcs)


def interactions_sprite_npcs(group):
    group_npcs = get_sprites_in_group(group)
    for npc in group_npcs:
        if (npc.type == "spawnkeeper"):
            if (npc.fully_woke == False):
                npc.interaction_init()



def hasArmorChestpiece(player, type):
    if type == "chestPiece":
        if (player_instance.chestPiece == False):
            player_instance.chestPiece = True
            player_instance.sheet = pg.image.load("images/player/playerChestPieceP.png").convert_alpha()
            return True
        return False




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
    screen.fill('black')
    screen.blit(game.current_bg_ac, (0,0))

    player.draw(screen)
    player.update()

    npcs.draw(screen)
    collision_sprite_npcs()
    SpawnKeeper_npc.update()


    monsters.draw(screen)
    monsters.update()

    collision_sprite_monsters()

    items.draw(screen)
    items.update()

    collided_items = collision_item()


    keys = pg.key.get_pressed()
    if keys[pg.K_e]:
        for item in collided_items:
            if (hasArmorChestpiece(player_instance, item.type)):
                items.remove(item)



    pg.display.update()
    clock.tick(60)


