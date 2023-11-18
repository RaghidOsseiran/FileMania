import pygame as pg

class Game:
    def __init__(self, screen):
        self.current_bg = pg.image.load("images/background/lvl1m.png").convert()
        self.current_bg_ac = pg.transform.scale(self.current_bg, (800, 457))
