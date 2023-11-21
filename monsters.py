import pygame as pg
import random
from items import *


class Monsters(pg.sprite.Sprite):
    def __init__(self, img_path, start_x, start_y, initial_stance, rect_surface, namegroup):
        super().__init__()
        self.sheet = pg.image.load(img_path).convert_alpha()
        self.image = self.sheet.subsurface(initial_stance)
        self.rect = self.image.get_rect(midbottom = rect_surface)
        self.initial_pos = (start_x, start_y)
        self.hasObject = False
        self.Item = 0
        self.type = ""
        namegroup.add(self)


class Sheep(Monsters):
    def __init__(self, start_x, start_y, gameself):
        self.game = gameself
        super().__init__("images/Npcs/Sheep/Sheep.png", start_x, start_y, pg.Rect(17, 207 + (64*8), 30, 47), (start_x,start_y), self.game.monster_group)
        self.hasObject = True
        self.moveRight = True
        self.lastPosX = 0
        self.lastPosY = 0
        self.type = "sheep"


        self.right_movement = []
        self.left_movement = []

        for i in range(8):
            self.right_movement.append(self.sheet.subsurface(pg.Rect(17+ (64*i), 207+(64*8), 30, 47)))
            self.left_movement.append(self.sheet.subsurface(pg.Rect(17+ (64*i), 207+(64*6), 30, 47)))
        self.movIndx = 0


    def collide_invis_border(self):
        if (self.rect.right == self.initial_pos[0]+170):
            self.moveRight = False  
        if (self.rect.left == self.initial_pos[1]+77):
            self.moveRight = True

    def movement(self):
        self.movIndx += 0.030
        if self.movIndx >= len(self.right_movement):
            self.movIndx = 0 
        if (self.moveRight):
            self.rect.right += 1
            self.image = self.right_movement[int(self.movIndx)]
        else:
            self.rect.left -= 1
            self.image = self.left_movement[int(self.movIndx)]


    def update(self):
        self.movement()
        self.collide_invis_border()
        self.movement()


class SpawnKeeper(Monsters):
    def __init__(self, start_x, start_y):
        super().__init__("images/Npcs/SpawnKeeper/SpawnKeeper.png",start_x, start_y, pg.Rect(338, 1291, 40, 53), (start_x, start_y))
        # in the super.init it enharits the self.sheet, self.image, self.rect.
        self.hasObject = True 
        self.type = "spawnkeeper"
        self.canInteract = False
        self.frame_interact = 0

        # array for the dialogue
        self.dialogue = ["press E to talk", "Hello sir, kill that sheep", "Oh, you dont have a weapon, here take my sword"]
        self.dialogueIndx = 0
        self.prv_key_state = False

        self.is_waking_up = False
        self.fully_woke = False



    # fonction pour gerer l'animation des wake up

    def wake_up_animation(self):
        wake_up = []
        for i in range (1,5):
            wake_up.append(self.sheet.subsurface(pg.Rect(338-(65*i), 1291, 40, 53)))
        wake_up.append(self.sheet.subsurface(pg.Rect(21, 713, 36, 53)))
        return wake_up
    
    def interaction_init(self):
        self.is_waking_up = True


    def wake_up(self):
        if self.is_waking_up:
            wake_up = self.wake_up_animation()
            if self.frame_interact < len(wake_up)-1 and not self.fully_woke:
                self.frame_interact += 0.2
                self.image = wake_up[int(self.frame_interact)]
            else:
                self.is_waking_up = False
                self.fully_woke = True


    
    def update(self):
        if not self.fully_woke:
            self.wake_up()
        

