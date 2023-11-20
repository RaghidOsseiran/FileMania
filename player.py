import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pg.image.load("images/player/playerSprites.png").convert_alpha()
        self.image = self.sheet.subsurface(pg.Rect(17, 207, 30, 47))
        self.rect = self.image.get_rect(midbottom = (233,438))

        player_stand_1_right = self.sheet.subsurface(pg.Rect(17, 207, 30, 47))
        player_stand_2_right = self.sheet.subsurface(pg.Rect(17+64, 207, 30, 47))

        player_stand_1_left = self.sheet.subsurface(pg.Rect(17, 207+(64*2), 30, 47))
        player_stand_2_left = self.sheet.subsurface(pg.Rect(17+64, 207+(64*2), 30, 47))

        self.player_stand_right = [player_stand_1_right,player_stand_2_right]
        self.player_stand_left = [player_stand_1_left,player_stand_2_left]
        self.player_standIndex = 0

        self.gravity = 0

        player_jump_right = self.sheet.subsurface(pg.Rect(17+(64*4), 207, 30, 47))
        player_jump_left = self.sheet.subsurface(pg.Rect(17+(64*5), 207-(64*2), 30, 47))
        self.player_jump_tab = [player_jump_right, player_jump_left]

        self.moveRight = True
    
    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d] and self.rect.right <= 805:
            self.rect.right += 3
            self.moveRight = True
        if keys[pg.K_q] and self.rect.left >= 0:
            self.rect.left -= 3
            self.moveRight = False
        if keys[pg.K_SPACE] and self.rect.bottom >= 438:
            self.gravity = -10

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 438:
            self.rect.bottom = 438


# jump 5*x et 4*y

    def animation_state_right(self):
        if self.rect.bottom < 438:
            if(self.moveRight):
                self.image = self.player_jump_tab[0]
            else:
                self.image = self.player_jump_tab[1]
        else:
            self.player_standIndex += 0.030
            if(self.player_standIndex >= len(self.player_stand_right)):
                self.player_standIndex = 0
            elif(self.moveRight):
                self.image = self.player_stand_right[int(self.player_standIndex)]
            else: self.image = self.player_stand_left[int(self.player_standIndex)]

        # else:


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state_right()


