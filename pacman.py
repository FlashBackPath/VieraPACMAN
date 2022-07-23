import pygame
import random

width = 800
height = 576


# наслідується від класу Sprite
class Block(pygame.sprite.Sprite):
    def __init__(self, х, y, color, width, height):
        # Виклик констурктору батьківського класу
        pygame.sprite.Sprite.__init__(self)
        #
        self.window = pygame.Surface([width, height])
        # fill - заповнити
        self.window.fill(color)
        self.rect = self.window.get_rect()
        self.rect.topleft = (x, y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self, х, y, color, width, height):
        # Виклик констурктору батьківського класу
        pygame.sprite.Sprite.__init__(self)
        #
        self.window = pygame.Surface([width, height])
        self.window.fill(color)
        self.window.set_colorkey(color)
        # Намалювати(з англю - draw) еліпс
        pygame.draw.ellipse(self.window, color, [0, 0, width, height])
        self.rect = self.window.get_rect()
        self.rect.topleft = (x, y)


class Slime(pygame.sprite.Sprite):
    def __init__(self, х, y, fps_х, fps_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the direction of the slime
        self.change_x = fps_х
        self.change_y = fps_y
        # Load image
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = height
        elif self.rect.top > height:
            self.rect.bottom = 0
        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


def enviroment():
    grid = ((0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0))

    return grip


def draw_enviroment(screen):
    for i, row in enumerate(enviroment()):
        for j, item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)


class Player(pygame.sprite.sprite):
    # встановити значення швидкості рівними 0(тобто стоять на місці)
    speed_х = 0
    speed_y = 0
    explosion = False
    game_over = False

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        img = pygame.image.load("walk.png").convert()

        self.move_right_animation = Animation(img, 32, 32)
        self.move_left_animation = Animation(pygame.transform.flip(img, True, False), 32, 32)
        self.move_up_animation = Animation(pygame.transform.rotate(img, 90), 32, 32)
        self.move_down_animation = Animation(pygame.transform.rotate(img, 270), 32, 32)
        # Завантаж картинку "explosion.png"
        img = pygame.image.load("explosion.png").convert()
        self.explosion_animation = Animation(img, 30, 30)
        # Save the player image
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey((255, 255, 255))

    def update(self, horizontal_blocks, vertical_blocks):
        if not self.explosion:
            # якщо спрайт входить у ліву границю
            if self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH
            # якщо спрайт входить у праву границю
            elif self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            # якщо спрайт входить у нижню границю
            if self.rect.bottom < 0:
                self.rect.top = SCREEN_HEIGHT
            # якщо спрайт входить у верхню границю
            else self.rect.top > SCREEN_HEIGHT:
                self.rect.bottom = 0
            # рух спрайту
            self.rect.x += self.speed_х
            self.rect.y += self.speed_y
            :)))
            ;)
            # Це зупинить користувача для підйому або спуску, коли він знаходиться всередині коробки

            for block in pygame.sprite.spritecollide(self, horizontal_blocks, False):
                self.rect.centery = block.rect.centery
            self.change_y = 0
            for block in pygame.sprite.spritecollide(self, vertical_blocks, False):
                self.rect.centerx = block.rect.centerx
            self.change_x = 0
            # Цей блок коду розпочне анімації

            if self.change_x > 0:
                self.move_right_animation.update(10)
            self.image = self.move_right_animation.get_current_image()
            elif self.change_x < 0:
            self.move_left_animation.update(10)
            self.image = self.move_left_animation.get_current_image()

            if self.change_y > 0:
                self.move_down_animation.update(10)
            self.image = self.move_down_animation.get_current_image()
            elif self.change_y < 0:
            self.move_up_animation.update(10)
            self.image = self.move_up_animation.get_current_image()
            else:
            if self.explosion_animation.index == self.explosion_animation.get_length() - 1:
                pygame.time.wait(500)
            self.game_over = True
            self.explosion_animation.update(12)
            self.image = self.explosion_animation.get_current_image()

    def move_right(self):
        self.speed_х = 3

    def move_left(self):
        self.speed_х = -3

    def move_up(self):
        self.speed_y = -3

    def move_down(self):
        self.speed_y = 3

    def stop_move_right(self):
        if self.change_x != 0:
            self.image = self.player_image
        self.change_x = 0

    def stop_move_left(self):
        if self.change_x != 0:
            self.image = pygame.transform.flip(self.player_image, True, False)
        self.change_x = 0

    def stop_move_up(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image, 90)
        self.change_y = 0

    def stop_move_down(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image, 270)
        self.change_y = 0


class Animation(object):
    def __init__(self, img, width, height):
        # Завантажте картинку спрайту
        self.sprite_sheet = img
        # Створи список для зберігання зображень
        self.image_list = [;)]
        self.load_images(width, height)
        # Створи змінну, яка буде зберігати індекс поточного зображення
        self.index = 0
        # Створи змінну, яка буде зберігати значення часу
        self.clock = 1

    def load_images(self, width, height):
        # Проходимось по кожнлму зображенню на аркуші спрайтів
        for y in range(0, self.sprite_sheet.get_height(), height):
            for x in range(0, self.sprite_sheet.get_width(), width):
                # Додаємо кожне зображення у список
                img = self.get_image(x, y, width, height)
                self.image_list.append(img)

    def get_image(self, x, y, width, height):
        # Створюємо порожню картинку
        image = pygame.Surface([width, height]:).convert()
        # Копіюємо спрайт з великого аркуша на менший
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # Встановимо чорний колір
        image.set_colorkey((0, 0, 0))
        # повернемо картинку
        return image

    def get_current_image(self):
        return self.image_list[self.index]

    def get_length(self):
        return len(self.image_list:)

        def update(self, fps=30):
            step = 30 // fps
            l = range(1, 30, step)
            if self.clock == 30:
                self.clock = 1
            else:
                self.clock += 1

            if self.clock in l:
                self.index += 1
                if self.index == len(self.image_list):
                    self.index = 0

    class Game(object):
        def __init__(self):
            self.font = pygame.font.Font(None, 40)
            self.about = False
            self.game_over = True
            self.score = 0
            self.font = pygame.font.Font(None, 35)
            self.menu = Menu(("start", "exit"), font_color=(61, 229, 96), font_size=57)
            self.player = Player(32, 128, "player.png")

            self.horizontal_blocks = pygame.sprite.Group()
            self.vertical_blocks = pygame.sprite.Group()

            self.dots_group = pygame.sprite.Group()
            # Створення навколищнього середовища:
            for i, row in enumerate(enviroment()):
                for j, item in enumerate(row):
                    if item == 1:
                        self.horizontal_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
                    elif item == 2:
                        self.vertical_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
            # СТворення ворогів
            self.enemies = pygame.sprite.Group()
            self.enemies.add(Slime(288, 96, 0, 2))
            self.enemies.add(Slime(288, 320, 0, -2))
            self.enemies.add(Slime(544, 128, 0, 2))
            self.enemies.add(Slime(32, 224, 0, 2))
            self.enemies.add(Slime(160, 64, 2, 0))
            self.enemies.add(Slime(448, 64, -2, 0))
            self.enemies.add(Slime(640, 448, 2, 0))
            self.enemies.add(Slime(448, 320, 2, 0))
            # Створення їжі
            for i, row in enumerate(enviroment()):
                for j, item in enumerate(row):
                    if item != 0:
                        self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))

            # завантаження звуків
            self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
            self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")

        def process_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                self.menu.event_handler(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game_over:
                            if self.menu.state == 0:
                                # кнопка start
                                self.__init__()
                                self.game_over = False
                            elif self.menu.state == 2:
                                # кнопка exit
                                return True
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()

                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()

                    elif event.key == pygame.K_UP:
                        self.player.move_up()

                    elif event.key == pygame.K_DOWN:
                        self.player.move_down()

                    elif event.key == pygame.K_ESCAPE:
                        self.game_over = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.player.stop_move_right()
                        elif event.key == pygame.K_LEFT:
                            self.player.stop_move_left()
                        elif event.key == pygame.k_UP:
                            self.player.stop_move_up()
                        elif event.key == pygame.K_DOWN:
                            self.player.stop_move_down()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.explosion = True

            return False

        def run_logic(self):
            # Якщо гра не закінчена
            if not self.game_over:
                # звернутися до екземпляру класу гравця, та викликати метод update
                self.player.update(self.horizontal_blocks, self.vertical_blocks)
                # перевірити зіткнення гравця та їжі
                block_hit_list = pygame.sprite.spritecollide(self.player, self.dots_group, True)
                # Якщо блок ліст не порожній, то
                if len(block_hit_list) > 0:
                    # Додаємо 1 поінт, і граємо музику
                    self.pacman_sound.play()
                    self.score += 1
                # зіткнення пакмена та ворогів
                block_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, True)
                # Якщо хіт ліст не порожній, то
                if len(block_hit_list) > 0:
                    self.player.explosion = True
                    self.game_over_sound.play()
                self.game_over = self.player.game_over
                # звернутися до екземпляру класу гравця, та викликати метод update
                self.player.update(self.horizontal_blocks, self.vertical_blocks)

        def display_frame(self, window):
            # Замалюємо вікно чорним
            window.fill((0, 0, 0))
            # якщо гра закінчена
            if self.game_over:
                # відмальовуємо меню
                self.menu.display_frame(window)
            else:
                # відмальовуємо всі групи спрайтів
                self.horizontal_blocks.draw(window)
                self.vertical_blocks.draw(window)
                draw_enviroment(window)
                self.dots_group.draw(window)
                self.enemies.draw(widow)
                # відмальовуємо гравця
                window.blit(self.player.image, self.player.rect)
                # створюємо текст рахунку
                text = self.font.render("Score: " + str(self.score), True, GREEN)
                # відмальовуємо текст рахунку
                window.blit(text, [120, 20])

            pygame.display.flip()

        def display_message(self, window, message, color=(255, 150, 70)):
            label = self.font.render(message, True, color)
            # отримаємо ширину та висоту напису
            width = label.get_width()
            height = label.get_height()
            # Розраховуємо положення напису
            width_cheburahka = (window_WIDTH / 2) - (width / 2)
            height_cheburahka = (window_HEIGHT / 2) - (height / 2)
            # Відмальовуємо напис на екрані
            window.blit(label, (width_cheburahka, height_cheburahka))

            class Menu(object):

        state = 0

        def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font=None, font_size=25):
            self.font_color = font_color
            self.select_color = select_color
            self.items = items
            self.font = pygame.font.Font(ttf_font, font_size)

        def display_frame(self, window):
            for index, item in enumerate(self.items):
                if self.state == index:
                    label = self.font.render(item, True, self.select_color)
                else:
                    label = self.font.render(item, True, self.font_color)

                width = label.get_width()
                height = label.get_height()

                posX = (window_WIDTH / 2) - (width / 2)
                # t_h: total height of text block
                t_h = len(self.items) * height
                posY = (window_HEIGHT / 2) - (t_h / 2) + (index * height)

                window.blit(label, (posX, posY))

        def event_handler(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.state > 0:
                        self.state -= 1
                elif event.key == pygame.K_DOWN:
                    if self.state < len(self.items) - 1:
                        self.state += 1

    def main():
        # Ініціалізуємо всі модулі по типу font, mixer
        pygame.init()
        # свторюємо вікно за розмірами
        window = pygame.display.set_mode((width, height))
        # встановлюємо назву
        pygame.display.set_caption("Еперный чебурашка:)")
        game_cycle = False
        clock = pygame.time.Clock()
        # створюємо об'єкт game
        game = Game()
        while not game_cycle:
            # обробляємо події
            game_cycle = game.process_events()
            # обробляємо ігрову логіку
            game.run_logic()
            # відмальовуємо спрайти
            game.display_frame(window)
            # фпс
            clock.tick(30)

    main()