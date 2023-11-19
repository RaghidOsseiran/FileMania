import pygame as pg
import random
from items import *


class Monsters(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "sheep":
            self.sheet = pg.image.load("images/Sheep/Sheep.png").convert_alpha()
            self.image = self.sheet.subsurface(pg.Rect(17, 207 + (64*8), 30, 47))
            self.rect = self.image.get_rect(midbottom = (585,438))
            self.hasObject = True
            self.moveRight = True
            self.lastPosX = 0
            self.lastPosY = 0
            self.Item = 0

            self.right_movement = []
            self.left_movement = []

            for i in range(8):
                self.right_movement.append(self.sheet.subsurface(pg.Rect(17+ (64*i), 207+(64*8), 30, 47)))
                self.left_movement.append(self.sheet.subsurface(pg.Rect(17+ (64*i), 207+(64*6), 30, 47)))
            self.movIndx = 0

            self.intial_pos = (585,425)

    def collide_invis_border(self):
        if (self.rect.right == 755):
            self.moveRight = False  
        if (self.rect.left == 515):
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


# from current pos x 8, 6 with y