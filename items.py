import pygame as pg


class Items(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()



class ChestPiece(Items):
    def __init__(self, posX, posY):
        super().__init__()
        self.sheet = pg.image.load("images/items/Chest2.png").convert_alpha()
        self.image = self.sheet.subsurface(pg.Rect(17,33, 30, 14))
        self.rect = self.image.get_rect(midbottom = (posX, posY+48))
        self.pickedUp = False
