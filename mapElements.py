import pygame
from pygame.sprite import Sprite


class Pole(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.image = pygame.Surface((20, 200))
        sheet = pygame.image.load('resources/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (320, 0, 20, 150))
        self.image = pygame.transform.scale(self.image, (60, 550))
        self.rect = self.image.get_rect()
        self.rect.x = 8002
        self.rect.y = 148

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Flag(Sprite):
    def __init__(self, screen, settings, stats):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.screen_rect = screen.get_rect()

        self.image = pygame.Surface((30, 30))
        sheet = pygame.image.load('resources/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (340, 0, 30, 16))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 7930
        self.rect.y = 170

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.stats.reached_pole and self.rect.y != 400:
            self.rect.y += 5
        if self.rect.y == 400:
            self.stats.flag_reach_bot = True


class Pipe(Sprite):
    def __init__(self, screen, settings, num):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.num = num
        self.screen_rect = screen.get_rect()

        self.pipe = []
        self.pipe_loc = [1150, 1450, 1800, 2260, 6600, 7200, 600, 550]
        self.height = [83, 125, 167, 167, 83, 83, 520, 264]
        self.image = pygame.Surface((40, 200))
        sheet = pygame.image.load('resources/allsprites.png')

        self.image.set_colorkey((0, 0, 0))
        self.image.blit(sheet, (0, 0), (200, 0, 40, 40))
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()

        temp_img1 = pygame.Surface((32, 33))
        temp_img1.set_colorkey((0, 0, 0))
        temp_img1.blit(sheet, (0, 0), (200, 0, 40, 40))
        temp1 = pygame.transform.scale(temp_img1, (80, 85))

        temp_img2 = pygame.Surface((32, 100))
        temp_img2.set_colorkey((0, 0, 0))
        temp_img2.blit(sheet, (0, 0), (200, 40, 40, 50))
        temp2 = pygame.transform.scale(temp_img2, (80, 260))

        temp_img3 = pygame.Surface((32, 200))
        temp_img3.set_colorkey((0, 0, 0))
        temp_img3.blit(sheet, (0, 0), (200, 90, 40, 80))
        temp3 = pygame.transform.scale(temp_img3, (80, 520))

        temp_img4 = pygame.Surface((30, 100))
        temp_img4.set_colorkey((0, 0, 0))
        temp_img4.blit(sheet, (0, 0), (273, 0, 30, 144))
        temp4 = pygame.transform.scale(temp_img4, (65, 260))

        temp_img5 = pygame.Surface((60, 40))
        temp_img5.set_colorkey((0, 0, 0))
        temp_img5.blit(sheet, (0, 0), (250, 144, 60, 50))
        temp5 = pygame.transform.scale(temp_img5, (130, 90))

        self.pipe.append(temp1)
        self.pipe.append(temp2)
        self.pipe.append(temp3)
        self.pipe.append(temp3)
        self.pipe.append(temp1)
        self.pipe.append(temp1)
        self.pipe.append(temp4)
        self.pipe.append(temp5)
        self.image = self.pipe[self.num]
        self.rect = self.image.get_rect()
        self.rect.x = self.pipe_loc[self.num]
        self.rect.y = self.settings.base_level - self.height[self.num]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Brick(Sprite):
    BRICK_SIZE = 40

    def __init__(self, screen, settings, block_type):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.block_type = block_type
        self.change_brick = False

        self.sz = Brick.BRICK_SIZE
        self.brick = "resources/Red_Brick.png"
        self.item_brick = "resources/Item_Brick.png"
        self.stone = "resources/Ground_Brick.png"
        self.stair_brick = "resources/Stair_Brick.png"
        self.empty_brick = "resources/Empty_Brick.png"
        self.invisible_brick = "resources/Invisible_Block.png"
        self.blue_brick = "resources/Blue_Brick.png"
        self.blue_stone = "resources/Blue_Stone.png"

        if block_type == 0:
            self.image = pygame.image.load(self.brick)
        if block_type == 1:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 2:
            self.image = pygame.image.load(self.item_brick)
        if block_type == 3:
            self.image = pygame.image.load(self.stone)
        if block_type == 4:
            self.image = pygame.image.load(self.stair_brick)
        if block_type == 5:
            self.image = pygame.image.load(self.brick)
        if block_type == 6:
            self.image = pygame.image.load(self.invisible_brick)
        if block_type == 7:
            self.image = pygame.image.load(self.blue_brick)
        if block_type == 8:
            self.image = pygame.image.load(self.blue_stone)
        if block_type == 9:
            self.image = pygame.image.load(self.brick)

        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.og_pos = self.rect.y
        self.frame_counter = 0
        self.bouncing = False

    def change(self):
        self.image = pygame.image.load(self.empty_brick)
        self.image = pygame.transform.scale(self.image, (self.sz, self.sz))

    def update(self):
        if self.bouncing:
            if self.frame_counter <= 5:
                self.rect.y -= 1
            elif self.frame_counter <= 10:
                self.rect.y += 1
            else:
                self.frame_counter = 0
                self.bouncing = False
            self.frame_counter += 1
