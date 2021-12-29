import sys
from moviepy.editor import *
import pygame
import os

FPS = 120
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# running = True


def load_image(name, color_key=None):
    full_name = os.path.join('data', name)
    if not os.path.isfile(full_name):
        raise FileNotFoundError(f"Файл {full_name} не найден")
    image = pygame.image.load(full_name)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = os.path.join("data", filename)
    # читаем уровень, убирая символы перевода строки
    with open(filename) as map_file:
        level_map = [line.strip() for line in map_file]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


collaid = load_image('Tile_02.png')
c = pygame.transform.scale(collaid, (100, 100))
i = load_image('idle.png')
idle = pygame.transform.scale(i, (100, 100))
car = load_image('car-full.png')
tile_images = {
    'wall': c,
    'empty': load_image('idle2.png'),
    'object': car
}
player_image = idle
car_image = car

tile_width = 100
tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# class Player(pygame.sprite.Sprite):
#     a = load_image('idle.png')
#     image = pygame.transform.scale(a, (200, 200))
#
#     def __init__(self, *groups):
#         super().__init__(player_group, all_sprites)
#         self.image = Player.image
#         self.rect = self.image.get_rect()
#         self.rect.x = 200
#         self.rect.y = 810
#         self.moving = True
#         self.isjump = False
#         self.jumpcount = 10
#
#     def update(self, *args, **kwargs):
#         keys = pygame.key.get_pressed()
#         # if keys[pygame.K_UP] and self.rect.y > 50:
#         #     # self.rect = self.rect.move(random.randint(-1, 1),
#         #     #                            random.randint(-1, 1))
#         #     self.rect.y -= 10
#         if keys[pygame.K_LEFT] and self.rect.x:  # > -10:
#             self.rect.x -= 15
#         if keys[pygame.K_RIGHT] and self.rect.x:  # < 1900:
#             self.rect.x += 15
#         if not(self.isjump):
#             if keys[pygame.K_DOWN] and self.rect.y < 800:
#                 self.rect.y += 15
#             if keys[pygame.K_UP]:
#                 self.isjump = True
#         else:
#             if self.jumpcount >= -10:
#                 if self.jumpcount < 0:
#                     self.rect.y += (self.jumpcount ** 2) // 2
#                 else:
#                     self.rect.y -= (self.jumpcount ** 2) // 2
#                 self.jumpcount -= 1
#             else:
#                 self.isjump = False
#                 self.jumpcount = 10

class Player(pygame.sprite.Sprite):
    right = True
    dx = (tile_width - player_image.get_width()) // 2
    dy = (tile_height - player_image.get_height()) // 4

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + Player.dx,
                                               tile_height * (pos_y - 0.5) + Player.dy)
        self.moving = True
        self.isjump = False
        self.jumpcount = 10

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        # self.calc_grav()
        if keys[pygame.K_LEFT] and self.rect.x:  # > -10:
            self.rect.x -= 15
            if self.right:
                self.flip()
                self.right = False
        if keys[pygame.K_RIGHT] and self.rect.x:  # < 1900:
            self.rect.x += 15
            if not self.right:
                self.flip()
                self.right = True

        if not self.isjump:
            if keys[pygame.K_DOWN] and self.rect.y:
                self.rect.y += 15
            if keys[pygame.K_UP]:
                self.isjump = True
        else:
            if self.jumpcount >= -10:
                if self.jumpcount < 0:
                    self.rect.y += (self.jumpcount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpcount ** 2) // 2
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 10

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def calc_grav(self):
        if self.rect.y == 0:
            self.rect.y = 1
        else:
            self.rect.y += 95
        if self.rect.y >= height - self.rect.height and self.rect.y >= 0:
            self.rect.y = 0
            self.rect.y = height - self.rect.height


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            # if level[y][x] == '.':
            #     Tile('empty', x, y)
            if level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '*':
                Tile('object', x, 20)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 1.2)


def terminate():
    pygame.quit()
    sys.exit()


small_font = pygame.font.SysFont('comicsansms', 25)
medium_font = pygame.font.SysFont('comicsansms', 50)
large_font = pygame.font.SysFont('comicsansms', 80)


def text_object(text, color, greatness):
    if greatness == 'small':
        text_surface = small_font.render(text, True, color)
    elif greatness == 'small':
        text_surface = medium_font.render(text, True, color)
    else:
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0, greatness='small'):
    text_surf, text_rect = text_object(msg, color, greatness)
    text_rect.center = (width / 2), (height / 2) + y_displace
    screen.blit(text_surf, text_rect)


def play_first_video():
    movie = pygame.movie.Movie('MELT.MPG')
    # screen = pygame.display.set_mode(movie.get_size())
    # movie_screen = pygame.Surface(movie.get_size()).convert()
    # movie.set_display(movie_screen)
    # movie.play()
    # playing = True
    # while playing:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             movie.stop()
    #             playing = False
    #     screen.blit(movie_screen,(0,0))
    #     pygame.display.update()
    #     clock.tick(FPS)
    # pygame.quit()

preview = True


def play_preview():
    video = VideoFileClip('data/final1.mp4')
    clip_resized = video.resize(height=900)
    global preview
    while preview:
        keys = pygame.key.get_pressed()
        clip_resized.preview(fps=15, fullscreen=True)
        for event in pygame.event.get():
            if keys[pygame.K_n]:
                preview = False
                break
                return


def start_screen():
    while True:
        keys = pygame.key.get_pressed()
        screen.fill('black')
        message_to_screen('Welcome to THE RETURNING OF EVIL',
                          'white',
                          -100,
                          'large')
        message_to_screen('Meet people, talk with them, complete their tasks and save the world!',
                          'white',
                          -30)
        message_to_screen('Press Y to start or Escape to quit.',
                          'white',
                          180)
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                terminate()
            if keys[pygame.K_y]:
                play_preview()

        pygame.display.flip()
        clock.tick(FPS)


player, level_x, level_y = generate_level(load_level('map.txt'))
camera = Camera()
start_screen()
while True:
    keys = pygame.key.get_pressed()
    bg = load_image('bg.jpg')
    bg1 = pygame.transform.scale(bg, (width, height))
    for event in pygame.event.get():
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            terminate()
        if keys[pygame.K_ESCAPE]:
            terminate()
        if event.type == pygame.KEYDOWN:
            player_group.update(event)
    screen.blit(bg1, (0, 0))
    camera.update(player)

    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.update()
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    print(clock.tick(FPS))
