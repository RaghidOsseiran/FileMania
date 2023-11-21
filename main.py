import pygame as pg
import sys
import random
import time
from game import *
from player import *
from monsters import *
from items import *




Game()




def draw_text(text, color, surface, x, y, AA):
    text_surface = items_font.render(text, AA, color)
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
            draw_text(collide_message, "white", screen, item.rect.x, item.rect.y, False)
    return collided_items


def collision_sprite_npcs():
    collided_npcs = pg.sprite.spritecollide(player.sprite, npcs, False)
    if collided_npcs:
        for npc in collided_npcs:
            # in case of spawnkeeper npc
            if (npc.hasObject and npc.type == "spawnkeeper"):
                keys = pg.key.get_pressed()
                key_pressed_E = keys[pg.K_e]
                if keys[pg.K_e] and not npc.fully_woke:
                    interactions_sprite_npcs(npcs)
                if npc.fully_woke:
                    draw_text(npc.dialogue[npc.dialogueIndx], 'white', screen, npc.rect.x, npc.rect.y, True)
                    dialogue_control(npc, key_pressed_E, npc.prv_key_state) 
                npc.prv_key_state = key_pressed_E
                

def interactions_sprite_npcs(group):
    group_npcs = get_sprites_in_group(group)
    for npc in group_npcs:
        if (npc.type == "spawnkeeper"):
            if (npc.fully_woke == False):
                npc.interaction_init()


def dialogue_control(npc, key_state_now, prv_key_state):
    if prv_key_state and not key_state_now:
        npc.dialogueIndx += 1
        if (npc.dialogueIndx > 2 ): # and sheep not killed (a ajouter)
            npc.dialogueIndx = 2
            draw_text("...", 'white', screen, npc.rect.x, npc.rect.y, True)





def hasArmorChestpiece(player, type):
    if type == "chestPiece":
        if (player_instance.chestPiece == False):
            player_instance.chestPiece = True
            player_instance.sheet = pg.image.load("images/player/playerChestPieceP.png").convert_alpha()
            return True
        return False





