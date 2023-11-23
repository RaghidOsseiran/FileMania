import pygame as pg
import sys
import random
import time
from game import *
from player import *
from monsters import *
from items import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800,457))
        pg.display.set_caption("FileMania")
        self.clock = pg.time.Clock()
        self.text_font = pg.font.Font("images/font/Pixeltype.ttf", 25)

        self.init_player()
        self.player_group = pg.sprite.GroupSingle(self.player)

        self.monster_group = pg.sprite.Group()
        self.npcs_group = pg.sprite.Group()
        self.items_group = pg.sprite.Group()

        self.init_sheep()
        self.init_spawnKeeper()





        self.current_bg = pg.image.load("images/background/lvl1m.png").convert()
        self.current_bg_ac = pg.transform.scale(self.current_bg, (800, 457))
        self.start()

    #player monsters and npc initialisations
    def init_player(self):
        self.player = Player(self)

    def init_sheep(self):
        self.SheepMonster = Sheep(585, 438,self)

    def init_spawnKeeper(self):
        self.spawnKeeper = SpawnKeeper(35,438, self)



    #utilitary function
    def get_sprites_in_group(group):
        return group.sprites()


    def draw_text(self, text, color, surface, x, y, AA):
        text_surface = self.text_font.render(text, AA, color)
        text_rect = text_surface.get_rect(topleft = (x, y-25))
        surface.blit(text_surface, text_rect)



    # collision detection + collision interactions




    def spawnItem(self, monster):
        monster.Item_dropped = ChestPiece(monster.lastPosX, monster.lastPosY, self)
        self.items_group.add(monster.Item_dropped)
        monster.kill()


    def collision_sprite_monsters(self):
        current_time = pg.time.get_ticks()
        collided_monsters = pg.sprite.spritecollide(self.player, self.monster_group, False)
        if collided_monsters:
            for monster in collided_monsters:
                if (monster.hasObject and monster.type == "sheep" and self.player.inventory["attackweapon"]):
                    monster.lastPosX = monster.rect.x
                    monster.lastPosY = monster.rect.y
                    monster.hasObject = False
                    self.spawnItem(monster)
                else:
                    print(f"timer between: {current_time - self.player.damage_cooldown}")
                    if current_time - self.player.damage_cooldown > self.player.damage_cooldown_period:
                        self.player.hp -= 5
                        self.player.damage_cooldown = current_time





    def collision_sprite_npcs(self):
        collided_npcs = pg.sprite.spritecollide(self.player, self.npcs_group, False)
        if collided_npcs:
            for npc in collided_npcs:
                # in case of spawnkeeper npc
                if (npc.hasObject and npc.type == "spawnkeeper"):
                    keys = pg.key.get_pressed()
                    key_pressed_E = keys[pg.K_e]
                    if keys[pg.K_e] and not npc.fully_woke:
                        self.interactions_sprite_npcs()
                    if npc.fully_woke and npc.dialogueIndx <= 4:
                        self.draw_text(npc.dialogue[npc.dialogueIndx], 'white', self.screen, npc.rect.x, npc.rect.y, True)
                        self.spawnKeeper.dialogue_control(npc, key_pressed_E, npc.prv_key_state) 
                    npc.prv_key_state = key_pressed_E
                    

    def interactions_sprite_npcs(self):
        for npc in self.npcs_group:
            if (npc.type == "spawnkeeper"):
                if (npc.fully_woke == False):
                    npc.interaction_init()

    def start(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
            self.screen.fill('black')
            self.screen.blit(self.current_bg_ac, (0,0))

            self.player_group.draw(self.screen)
            self.player.update()

            self.npcs_group.draw(self.screen)
            self.collision_sprite_npcs()
            self.npcs_group.update()


            self.monster_group.draw(self.screen)
            self.monster_group.update()
            self.collision_sprite_monsters()

            self.items_group.draw(self.screen)
            self.items_group.update()


            pg.display.update()
            self.clock.tick(60)
