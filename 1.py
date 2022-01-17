from moviepy.editor import *
import pygame
import os

FPS = 120
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
current_level = 1
anim_sprite = pygame.sprite.Group()


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


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, fps):
        super().__init__(anim_sprite)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.counter = 0
        self.limit = FPS // fps
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for i in range(rows):
            for j in range(columns):
                frame_location = (self.rect.w * j, self.rect.h * i)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.counter += 1
        if self.counter == self.limit:
            self.counter = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


dragon = AnimatedSprite(load_image("B_witch_idle.png"), 1, 6, 50, 50, 10)

collaid = load_image('Tile_02.png')
earth = pygame.transform.scale(collaid, (100, 100))
player = load_image('idle.png')
idle = pygame.transform.scale(player, (100, 100))
big_accurate_tree = pygame.transform.scale(load_image('big_tree.png'), (350, 500))
small_accurate_tree = pygame.transform.scale(load_image('small_tree.png'), (200, 200))
big_tree_disheveled = pygame.transform.scale(load_image('big_tree_1.png'), (450, 600))
small_tree_disheveled = pygame.transform.scale(load_image('small_tree_1.png'), (200, 200))
barrel = pygame.transform.scale(load_image('barrel.png'), (50, 50))
pit = pygame.transform.scale(load_image('pit.png'), (300, 200))
pitchers = load_image('pitchers.png')
bush_accurate = load_image('bush.png')
bush_disheveled = load_image('bush1.png')
sunflowers = pygame.transform.scale(load_image('sunflowers.png'), (150, 100))
scarecrows = load_image('scarecrows.png')
wheat = load_image('wheat.png')
bench = load_image('bench.png')
logs = pygame.transform.scale(load_image('logs.png'), (250, 250))
pumpkins = pygame.transform.scale(load_image('pumpkins.png'), (150, 100))
signpost = pygame.transform.scale(load_image('signpost.png'), (80, 150))
house1 = load_image('house2.png')
house2 = load_image('house3.png')
witch = load_image('witch.png')
witch1 = pygame.transform.scale(witch, (100, 100))
tile_images_for_first_level = {
    'wall': earth,
    'big_accurate_tree': big_accurate_tree,
    'small_accurate_tree': small_accurate_tree,
    'big_tree_disheveled': big_tree_disheveled,
    'small_tree_disheveled': small_tree_disheveled,
    'barrel': barrel,
    'pit': pit,
    'pitchers': pitchers,
    'bush_accurate': bush_accurate,
    'bush_disheveled': bush_disheveled,
    'sunflowers': sunflowers,
    'scarecrows': scarecrows,
    'wheat': wheat,
    'bench': bench,
    'logs': logs,
    'pumpkins': pumpkins,
    'signpost': signpost,
    'house1': house1,
    'house2': house2,
    "witch": witch1
}
earth_2 = pygame.transform.scale(load_image('small_earth.png'), (250, 200))
stone_1 = load_image('stone_1.png')
branch_with_thorns_1 = load_image('branch_with_thorns.png')
plant_1 = load_image('plant_1.png')
plant_2 = load_image('plant_2.png')
plant_3 = load_image('plant_3.png')
plant_4 = load_image('plant_4.png')
plant_5 = load_image('plant_5.png')
plant_6 = load_image('plant_6.png')
plant_column = load_image('plant_column.png')
stone_2 = load_image('stone_2.png')
stone_3 = load_image('stone_3.png')
blue_flower = load_image('Bluef.png')
plant_7 = load_image('jump_p.png')
tile_images_for_second_level = {
    'wall': earth_2,
    'stone_1': stone_1,
    'branch_with_thorns_1': branch_with_thorns_1,
    'plant_1': plant_1,
    'blue_flower': blue_flower,
    'plant_7': plant_7,
    'plant_2': plant_2,
    'plant_3': plant_3,
    'plant_4': plant_4,
    'plant_5': plant_5,
    'plant_6': plant_6,
    'plant_column': plant_column,
    'stone_2': stone_2,
    'stone_3': stone_3
}
earth_3 = load_image('floor_2.png')
hill = load_image('hill.png')
rock_1 = load_image('rock_1.png')
rock_2 = load_image('rock_2.png')
small_pl = load_image('small_pl.png')
grass = load_image('Grass.png')
grass_2 = load_image('Grass_2.png')
grass_3 = load_image('Grass_3.png')
plants_group = load_image('plants_group.png')
high_rock = load_image('rock_h.png')
stalagmites = load_image('stalagmites.png')
rock_3 = load_image('rock_3.png')
rock_4 = load_image('rock_4.png')
sharp_columns = load_image('sharp_columns.png')
tile_images_for_third_level = {
    'wall': earth_3,
    'hill': hill,
    'rock_1': rock_1,
    'rock_2': rock_2,
    'small_pl': small_pl,
    'grass': grass,
    'grass_2': grass_2,
    'grass_3': grass_3,
    'plants_group': plants_group,
    'high_rock': high_rock,
    'stalagmites': stalagmites,
    'rock_3': rock_3,
    'rock_4': rock_4,
    'sharp_columns': sharp_columns
}
player_image = idle

tile_width = 100
tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if current_level == 1:
            self.image = tile_images_for_first_level[tile_type]
        elif current_level == 2:
            self.image = tile_images_for_second_level[tile_type]
        elif current_level == 3:
            self.image = tile_images_for_third_level[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


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


pers_groups = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            # if level[y][x] == '.':
            #     Tile('empty', x, y)
            if level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '*':
                Tile('pit', x, 21.6)
            elif level[y][x] == '%':
                new_player = Player(x, y)
            elif level[y][x] == "[":
                Tile('barrel', x, 24.1)
            elif level[y][x] == '{':
                Tile('house1', x, 15)
            elif level[y][x] == '+':
                Tile('signpost', x + 0.3, 22.8)
            elif level[y][x] == '"':
                Tile('pitchers', x - 1, 24.23)
            elif level[y][x] == ':':
                Tile('logs', x, 21.6)
            elif level[y][x] == "'":
                Tile('house2', x, 15)
            elif level[y][x] == ")":
                Tile('big_accurate_tree', x, 16)
            elif level[y][x] == "(":
                Tile('big_tree_disheveled', x, 14)
            elif level[y][x] == "/":
                Tile('bench', x, 24.1)
            elif level[y][x] == "!":
                Tile('pumpkins', x, 23.6)
            elif level[y][x] == "-":
                Tile('sunflowers', x, 23.4)
            elif level[y][x] == "=":
                Tile('scarecrows', x, 23)
            elif level[y][x] == "]":
                Tile('bush_accurate', x, 24.3)
            elif level[y][x] == "?":
                Tile('wheat', x, 23.4)
            elif level[y][x] == "l":
                Tile('bush_disheveled', x, 24.1)
            elif level[y][x] == "f":
                Tile('small_tree_disheveled', x, 21.3)
            elif level[y][x] == "v":
                Tile('small_accurate_tree', x, 21.5)
            elif level[y][x] == "w":
                # a = AnimatedSprite(witch1, 1, 6, x, 23.31, 10)
                Tile("witch", x, 23.31)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def generate_level_2(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            # if level[y][x] == '.':
            #     Tile('empty', x, y)
            # new_player = Player(x, y)
            if level[y][x] == '%':
                new_player = Player(x, 24.5)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '[':
                Tile('stone_1', x, 10)
            elif level[y][x] == '|':
                Tile('plant_column', x, 1)
            elif level[y][x] == ')':
                Tile('branch_with_thorns_1', x, 12)
            elif level[y][x] == '+':
                Tile('plant_1', x, 19)
            elif level[y][x] == 'p':
                Tile('plant_2', x, 19)
            elif level[y][x] == ']':
                Tile('stone_2', x, 9)
            elif level[y][x] == '*':
                Tile('plant_3', x, 19)
            elif level[y][x] == '-':
                Tile('plant_4', x, 17)
            elif level[y][x] == '&':
                Tile('blue_flower', x, 10)
            elif level[y][x] == '^':
                Tile('stone_3', x, 9)
            elif level[y][x] == '$':
                Tile('plant_5', x, 17)
            elif level[y][x] == '@':
                Tile('plant_6', x, 16)
            elif level[y][x] == '!':
                Tile('plant_7', x, 19)
    return new_player, x, y


def generate_level_3(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '%':
                new_player = Player(x, 24.5)
            elif level[y][x] == '#':
                Tile('wall', x, 24.5)
            elif level[y][x] == 'h':
                Tile('hill', x, 22.3)
            elif level[y][x] == 'r':
                Tile('rock_1', x, 22)
            elif level[y][x] == ']':
                Tile('rock_2', x, 14)
            elif level[y][x] == '[':
                Tile('small_pl', x, 21.5)
            elif level[y][x] == '^':
                Tile('grass', x, 21.5)
            elif level[y][x] == '_':
                Tile('grass_2', x, 17)
            elif level[y][x] == '-':
                Tile('grass_3', x, 8)
            elif level[y][x] == 'p':
                Tile('plants_group', x, 21.5)
            elif level[y][x] == 'u':
                Tile('high_rock', x, 10)
            elif level[y][x] == 's':
                Tile('stalagmites', x, 15)
            elif level[y][x] == '3':
                Tile('rock_3', x, 16)
            elif level[y][x] == '4':
                Tile('rock_4', x, 17)
            elif level[y][x] == 'k':
                Tile('sharp_columns', x, 15)
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
                return
        pygame.display.flip()
        clock.tick(FPS)


def Dialog_One(player, npc):
    if npc.rect.x - player.rect.x == 2:
        pass



if current_level == 1:
    player, level_x, level_y = generate_level(load_level('map.txt'))
elif current_level == 2:
    player, lavel_x, level_y = generate_level_2(load_level('map_2.txt'))
elif current_level == 3:
    player, lavel_x, level_y = generate_level_3(load_level('map_3.txt'))
camera = Camera()
start_screen()
while True:
    keys = pygame.key.get_pressed()
    if current_level == 1:
        bg = load_image('b3_first.jpg')
    elif current_level == 2:
        bg = load_image('fon_2lvl.jpg')
    elif current_level == 3:
        bg = load_image('fon5.jpg')
    bg1 = pygame.transform.scale(bg, (width, height))
    for event in pygame.event.get():
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            terminate()
        if keys[pygame.K_ESCAPE]:
            terminate()
        if keys[pygame.K_1]:
            current_level = 1
            tiles_group.empty()
            player.kill()
            player, level_x, level_y = generate_level(load_level('map.txt'))
        if keys[pygame.K_2]:
            current_level = 2
            tiles_group.empty()
            player.kill()
            player, lavel_x, level_y = generate_level_2(load_level('map_2.txt'))
        if keys[pygame.K_3]:
            current_level = 3
            tiles_group.empty()
            player.kill()
            player, lavel_x, level_y = generate_level_3(load_level('map_3.txt'))
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
    anim_sprite.draw(screen)
    anim_sprite.update()
    clock.tick(FPS)

