import pygame as pg

class Game:
    def __init__(self, screen):
        self.current_bg = pg.image.load("images/background/lvl1.jpg").convert()
