import pygame
import os
import sys

FPS = 120
pygame.init()
size = width, height = 1920, 1080  # size of screen
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
current_level = 1
anim_sprite = pygame.sprite.Group()
# добавляем в микшер музыку всех уровней
first_level_music = pygame.mixer.Sound('data/music/first_level.mp3')
second_level_music = pygame.mixer.Sound('data/music/second_level.mp3')
third_level_music = pygame.mixer.Sound('data/music/third_level.mp3')


def load_image(name, color_key=None):  # Функция загрузки изображений
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


def load_level(filename):  # Функция загрузки уровней
    filename = os.path.join("data", filename)
    # читаем уровень, убирая символы перевода строки
    with open(filename) as map_file:
        level_map = [line.strip() for line in map_file]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class AnimatedSprite(pygame.sprite.Sprite):  # Класс анимированных спрайтов
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

    def update(self, *args, **kwargs):
        self.counter += 1
        if self.counter == self.limit:
            self.counter = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


# Блок загрузки всех изображений для первого уровня и границ уровней
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
b = load_image('Grass.png')
block = pygame.transform.scale(b, (150, 400))
b2 = load_image('Grass.png')
block2 = pygame.transform.scale(b2, (150, 400))
tile_images_for_first_level = {  # Словарь с изображениями для первого уровня
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
    'house2': house2
}
# Блок загрузки всех изображений для второго уровня
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
tile_images_for_second_level = {  # Словарь с изображениями для второго уровня
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
# Блок загрузки всех изображений для третьего уровня
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
tile_images_for_third_level = {  # Словарь с изображениями для третьего уровня
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
player_image = idle  # Картинка персонажа
block_image = block  # Первая граница
block_image2 = block2  # Вторая граница
block = 0

tile_width = 100
tile_height = 50


class Tile(pygame.sprite.Sprite):  # Класс тайлов
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


class Player(pygame.sprite.Sprite):  # Класс игрока
    global block
    global block2
    right = True
    dx = (tile_width - player_image.get_width()) // 2
    dy = (tile_height - player_image.get_height()) // 4

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + Player.dx,
                                               tile_height * (pos_y - 0.5) + Player.dy)
        self.mask = pygame.mask.from_surface(self.image)
        self.moving = True
        self.isjump = False
        self.jumpcount = 10

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        # self.calc_grav()
        if pygame.sprite.collide_mask(self, block):
            if keys[pygame.K_RIGHT]:  # < 1900:
                if keys[pygame.K_RIGHT] and keys[pygame.K_w]:
                    self.rect.x += 30
                else:
                    self.rect.x += 15
                if not self.right:
                    self.flip()
                    self.right = True
        elif pygame.sprite.collide_mask(self, block2):
            if keys[pygame.K_LEFT]:
                if keys[pygame.K_LEFT] and keys[pygame.K_w]:
                    self.rect.x -= 30
                else:
                    self.rect.x -= 15
                if self.right:
                    self.flip()
                    self.right = False
        else:
            if keys[pygame.K_LEFT]:
                if keys[pygame.K_LEFT] and keys[pygame.K_w]:
                    self.rect.x -= 30
                else:
                    self.rect.x -= 15
                if self.right:
                    self.flip()
                    self.right = False
            if keys[pygame.K_RIGHT]:  # < 1900:
                if keys[pygame.K_RIGHT] and keys[pygame.K_w]:
                    self.rect.x += 30
                else:
                    self.rect.x += 15
                if not self.right:
                    self.flip()
                    self.right = True

            if not self.isjump:
                if keys[pygame.K_UP]:
                    self.isjump = True
            else:
                # jump_sound.play()
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


def generate_level(level):  # Генерация первого уровня
    new_player, x, y = None, None, None
    global block
    global block2
    for y in range(len(level)):
        for x in range(len(level[y])):
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
            elif level[y][x] == 'g':
                block = Block(x, y - 2.9)
            elif level[y][x] == 'z':
                block2 = Block2(x - 0.7, y - 2.9)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def generate_level_2(level):  # Генерация второго уровня
    new_player, x, y = None, None, None
    global block
    global block2
    for y in range(len(level)):
        for x in range(len(level[y])):
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
            elif level[y][x] == 'g':
                block = Block(x, y - 2.5)
            elif level[y][x] == 'z':
                block2 = Block2(x, y - 2.5)
    return new_player, x, y


def generate_level_3(level):  # Генерация третьего уровня
    new_player, x, y = None, None, None
    global block
    global block2
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
            elif level[y][x] == 'g':
                block = Block(x, y - 2.5)
            elif level[y][x] == 'z':
                block2 = Block2(x, y - 2.5)
    return new_player, x, y


# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


class Camera:  # Класс камеры
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


def terminate():  # Закрытие игры
    pygame.quit()
    sys.exit()


# Блок обозначения величины шрифтов
small_font = pygame.font.SysFont('comicsansms', 25)
medium_font = pygame.font.SysFont('comicsansms', 50)
large_font = pygame.font.SysFont('comicsansms', 80)


def text_object(text, color, greatness):  # Создание текстового объекта
    if greatness == 'small':
        text_surface = small_font.render(text, True, color)
    elif greatness == 'medium':
        text_surface = medium_font.render(text, True, color)
    else:
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0, greatness='small'):  # Отображение сообщения на экране
    # y_displace - перемещение игрика вверх или вниз от центра экрана
    text_surf, text_rect = text_object(msg, color, greatness)
    text_rect.center = (width / 2), (height / 2) + y_displace
    screen.blit(text_surf, text_rect)


def start_screen():  # Экран начала игры
    c = pygame.image.load('data/cursor.png')  # Загрузка нового изображения курсора
    cursor = pygame.transform.flip(c, True, False)
    pygame.mouse.set_visible(False)  # hide the cursor

    pygame.mixer.music.load('data/music/3.mp3')
    pygame.mixer.music.play(loops=-1, fade_ms=60)  # Запуск музыки
    a = pygame.mixer.Sound('data/music/perehod.wav')
    while True:
        keys = pygame.key.get_pressed()
        screen.fill('black')
        message_to_screen('THE RETURNING OF EVIL',
                          'white',
                          -100,
                          'large')
        message_to_screen('Нажми Y, чтобы начать игру или Escape, чтобы выйти.',
                          'white',
                          390)
        message_to_screen('Управление - стрелочки, переключение уровней - клавиши 1, 2, 3',
                          'white',
                          20)
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                terminate()
            if keys[pygame.K_y]:
                pygame.mixer.music.stop()
                a.play()
                a.set_volume(0.5)
                first_level_music.play(loops=-1)
                first_level_music.set_volume(0.5)
                return
        coord = pygame.mouse.get_pos()
        screen.blit(cursor, coord)
        pygame.display.flip()
        clock.tick(FPS)


block_group = pygame.sprite.Group()  # Группа границ


class Block(pygame.sprite.Sprite):  # Класс первых границ
    dx = (tile_width - block_image.get_width()) // 2
    dy = (tile_height - block_image.get_height()) // 4

    def __init__(self, pos_x, pos_y):
        super().__init__(block_group, all_sprites)
        self.image = block_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + Block.dx,
                                               tile_height * (pos_y - 0.5) + Block.dy)
        self.mask = pygame.mask.from_surface(self.image)


class Block2(pygame.sprite.Sprite):  # Класс вторых границ
    dx = (tile_width - block_image2.get_width()) // 2
    dy = (tile_height - block_image2.get_height()) // 4

    def __init__(self, pos_x, pos_y):
        super().__init__(block_group, all_sprites)
        self.image = block_image2
        self.rect = self.image.get_rect().move(tile_width * pos_x + Block2.dx,
                                               tile_height * (pos_y - 0.5) + Block2.dy)
        self.mask = pygame.mask.from_surface(self.image)


def draw():  # Отображение анимированных персонажей
    witch_anim = load_image('anim/B_witch_idle.png')
    witch1_anim = pygame.transform.scale(witch_anim, (64, 576))
    fantasywarrior = load_image("anim/fantasywarrior.png")
    fantasywarrior2 = pygame.transform.scale(fantasywarrior, (3240, 324))
    medievalwarrior_blue = load_image("anim/medievalwarrior(blue).png")
    medievalwarrior_blue2 = pygame.transform.scale(medievalwarrior_blue, (2700, 270))
    medievalwarrior_gray = load_image("anim/medievalwarrior(gray).png")
    medievalwarrior_gray2 = pygame.transform.scale(medievalwarrior_gray, (1472, 182))
    medievalwarrior_red = load_image("anim/medievalwarrior(red).png")
    medievalwarrior_red2 = pygame.transform.scale(medievalwarrior_red, (2400, 300))
    spr_KingIdle_strip_no_bkg = load_image("anim/spr_KingIdle_strip_no_bkg.png")
    spr_KingIdle_strip_no_bkg2 = pygame.transform.scale(spr_KingIdle_strip_no_bkg, (4608, 256))
    wizard = load_image("anim/wizard.png")
    img = load_image("anim/spritesheet.png")
    img2 = pygame.transform.scale(img, (300, 100))
    AnimatedSprite(img2, 3, 1, 210, 800, 4)
    AnimatedSprite(witch1_anim, 1, 6, 380, 820, 6)
    AnimatedSprite(fantasywarrior2, 10, 1, 460, 700, 10)
    AnimatedSprite(medievalwarrior_blue2, 10, 1, 700, 735, 10)
    AnimatedSprite(medievalwarrior_gray2, 6, 1, 920, 740, 10)
    AnimatedSprite(medievalwarrior_red2, 8, 1, 1100, 720, 10)
    AnimatedSprite(spr_KingIdle_strip_no_bkg2, 18, 1, 1320, 760, 10)
    AnimatedSprite(wizard, 6, 1, 1540, 770, 6)


def victory_screen():  # Экран завершения игры
    draw()
    first_level_music.stop()
    second_level_music.stop()
    third_level_music.stop()
    pygame.mixer.music.load('data/music/2.mp3')
    pygame.mixer.music.play(loops=-1, start=56.8)  # Включение музыки
    while True:
        keys = pygame.key.get_pressed()
        screen.fill((193, 0, 32))
        message_to_screen('Спасибо за игру!',
                          'white',
                          -100,
                          'large')
        message_to_screen('Вы отлично справились!!!',
                          'white',
                          -30)
        message_to_screen('Чтобы выйти, нажмите Escape',
                          'white',
                          180)
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                terminate()
        anim_sprite.draw(screen)
        anim_sprite.update()
        pygame.display.flip()
        clock.tick(FPS)


player, level_x, level_y = generate_level(load_level('map.txt'))  # Отрисовка первого уровня
camera = Camera()
start_screen()
pygame.mouse.set_visible(False)  # делаем курсор мыши невидимым
while True:
    keys = pygame.key.get_pressed()
    # Присваивание фона каждому уровню
    if current_level == 1:
        bg = load_image('fon1_1_1.jpg')
    elif current_level == 2:
        bg = load_image('fon_2lvl.jpg')
    elif current_level == 3:
        bg = load_image('fon5.jpg')
    bg1 = pygame.transform.scale(bg, (width, height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if keys[pygame.K_ESCAPE]:
            victory_screen()
            terminate()
        # Загрузка уровней по кнопкам 1, 2, 3
        if keys[pygame.K_1]:
            current_level = 1
            third_level_music.stop()
            second_level_music.stop()
            first_level_music.play()
            tiles_group.empty()
            player.kill()
            block_group.empty()
            player, level_x, level_y = generate_level(load_level('map.txt'))
        if keys[pygame.K_2]:
            current_level = 2
            first_level_music.stop()
            third_level_music.stop()
            second_level_music.play(loops=-1)
            tiles_group.empty()
            player.kill()
            block_group.empty()
            player, lavel_x, level_y = generate_level_2(load_level('map_2.txt'))
        if keys[pygame.K_3]:
            current_level = 3
            second_level_music.stop()
            first_level_music.stop()
            third_level_music.play(loops=-1)
            tiles_group.empty()
            player.kill()
            block_group.empty()
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
    block_group.draw(screen)
    pygame.display.flip()
    anim_sprite.draw(screen)
    anim_sprite.update()
    clock.tick(FPS)
