import pygame as pg
import random
from items import *


class Monsters(pg.sprite.Sprite):
    def __init__(self, img_path, start_x, start_y):
        super().__init__()
        self.sheet = pg.image.load(img_path).convert_alpha()
        self.image = self.sheet.subsurface(pg.Rect(17, 207 + (64*8), 30, 47))
        self.rect = self.image.get_rect(midbottom = (start_x,start_y))

class Sheep(Monsters):
    def __init__(self, start_x, start_y):
        super().__init__("images/Sheep/Sheep.png", start_x, start_y)
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