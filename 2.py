import pygame
import os
import sys


FPS = 60
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

def load_image(name, color_key=None):
    full_name = os.path.join('data', name)
    if not os.path.isfile(full_name):
        raise FileNotFoundError(f"Файл {full_name} yt yfqltyj")
    image = pygame.image.load(full_name)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Gamer(pygame.sprite.Sprite):
    a = load_image('idle.png')
    image = pygame.transform.scale(a, (200, 200))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Gamer.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 800
        self.moving = True
        self.isjump = False
        self.jumpcount = 15

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] and self.rect.y > 50:
        #     # self.rect = self.rect.move(random.randint(-1, 1),
        #     #                            random.randint(-1, 1))
        #     self.rect.y -= 10
        if keys[pygame.K_DOWN] and self.rect.y < 800:
            self.rect.y += 10
        if keys[pygame.K_LEFT] and self.rect.x > 100:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT] and self.rect.x < 1600:
            self.rect.x += 10
        if not(self.isjump):
            if keys[pygame.K_UP]:
                self.isjump = True
        else:
            if self.jumpcount >= -15:
                if self.jumpcount < 0:
                    self.rect.y += (self.jumpcount ** 2) / 3
                else:
                    self.rect.y -= (self.jumpcount ** 2) / 3
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 15

all_sprites = pygame.sprite.Group()

for _ in range(5):
    Gamer(all_sprites)

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False
    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()