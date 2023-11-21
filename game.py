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

        self.init_player()

        self.monster_group = pg.sprite.Group()



        #to be cleaned
        npcs = pg.sprite.Group()
        SpawnKeeper_npc = SpawnKeeper(35,438)
        npcs.add(SpawnKeeper_npc)



        #Items group
        items = pg.sprite.Group()

        items_font = pg.font.Font("images/font/Pixeltype.ttf", 20)
        self.current_bg = pg.image.load("images/background/lvl1m.png").convert()
        self.current_bg_ac = pg.transform.scale(self.current_bg, (800, 457))
        self.player = Player(self)
        self.start()

    
    def init_player(self):
        self.player = Player(self)

    def init_sheep(self):
        self.SheepMonster = Sheep(585, 438,self)


    def start(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
            self.screen.fill('black')
            screen.blit(game.current_bg_ac, (0,0))

            player.draw(screen)
            player.update()

            npcs.draw(screen)
            collision_sprite_npcs()
            npcs.update()


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
