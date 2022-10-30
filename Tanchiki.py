import pygame 
from random import randint
import sys
pygame.init()

pygame.mixer.music.load("fon.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 800, 600 # Размер окна
FPS = 60
TILE = 32 # Размер всех картинок

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen = pygame.Surface((800, 640)) # размер меню
info = pygame.Surface((800, 30)) # размер информации в меню


fontUI = pygame.font.Font(None, 30)

# загрузка картинок
imgBrick = pygame.image.load('block_brick.png')
imgTanks = [
    pygame.image.load('tank1.png'),
    pygame.image.load('tank2.png'),
    pygame.image.load('tank3.png'),
    pygame.image.load('tank4.png'),
    pygame.image.load('tank5.png'),
    pygame.image.load('tank6.png'),
    pygame.image.load('tank7.png'),
    pygame.image.load('tank8.png'),
    ]
imgBangs = [
    pygame.image.load('bang1.png'),
    pygame.image.load('bang2.png'),
    pygame.image.load('bang3.png'),
    ]
imgBonuses = [
    pygame.image.load('bonus_star.png'),
    pygame.image.load('bonus_tank.png'),
    ]

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]] # Смещение в соответствующее направление (Вверх, Вправо, Вниз, Влево)

# параметры танков после взятия бонусов
MOVE_SPEED =    [1, 2, 2, 1, 2, 3, 3, 2]
BULLET_SPEED =  [4, 5, 6, 5, 5, 5, 6, 7]
BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
SHOT_DELAY =    [60, 50, 30, 40, 30, 25, 25, 30]
white = (255,255,255)
black = (0,0,0)
cvet = (0x74,0x85,0x88)


# процедура вывода на экран правил игры
def pravila(window):
    window.blit(screen, (0, 30))

    pravila_ = True
    pravila_menu_fnt = pygame.font.Font(None, 30) # размер текста
    while pravila_:
        
        window.blit(screen, (0, 0))
        screen.fill((white))  # фон правил
        
        # сам текст правил игры
        line = [" " for i in range(10)] # создание массива строк
        line[0]='Правила игры.'
        line[1]='«Танчики» - это игра, в которой два игрока управляют'
        line[2]='маленькими танками, и с помощью них должны уничтожить'
        line[3]='друг друга. Игра представлена на игровом поле, '
        line[4]='в котором разбросаны блоки в виде кирпичей, которые '
        line[5]='будут защищать игроков от пули (блоки уничтожаются'
        line[6]='с 1 выстрела). Ещё в игре время от времени появляются'
        line[7]='бонусы, которые дают игрокам разные преимущества.  '
        line[8]='   '
        line[9]=' Нажмите любую клавишу для возврата в меню... '
        
        for i in range(10):
            stroka = pravila_menu_fnt.render(line[i],1,cvet)
            window.blit(stroka,(80,40+i*30))  # расположение текста на экране

    
        
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()   # выход из программы
                # при нажатии любой клавиши клавиатуры или мыши - цикл
                # while заканчивается и возврат в меню
                if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                    pravila_ = False  # признак выхода из цикла while
                       
        pygame.display.flip()
        
        
# процедура вывода на экран информации об управлении игрой
def upravlenie(window):
    window.blit(screen, (0, 30))


    upravl_ = True
    upravl_menu_fnt = pygame.font.Font(None, 30) # размер текста
    while upravl_:
        
        window.blit(screen, (0, 0))
        screen.fill((white))  # фон управления
        
        # сам текст "управление"
        line = [" " for i in range(11)]  # создание массива строк
        line[0]='Управление.'
        line[1]='1 танк: движение вверх, вниз, вправо, влево - \"W\",\"A\",\"S\",\"D\";'
        line[2]='стрельба - \"Пробел\".'
        line[3]='   '
        line[4]='2 танк: движение вверх, вниз, вправо, влево - Стрелки на клавиатуре; '
        line[5]='стрельба - правый \"Enter\".'
        line[6]='   '
        line[7]='В левой части экрана 1 танк - синий,'
        line[8]='в правой части экрана 2 танк - красный.'
        line[9]='   '
        line[10]='Нажмите любую клавишу для возврата в меню...'
        
        for i in range(11):
            stroka = upravl_menu_fnt.render(line[i],1,cvet)
            window.blit(stroka,(80,40+i*30)) # расположение текста на экране

    
        
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()   # выход из программы
                # при нажатии любой клавиши клавиатуры или мыши - цикл
                # while заканчивается и возврат в меню
                if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
                    upravl_ = False
                       
        pygame.display.flip()





class UI: # пользовательский интерфейс
    def __init__(self):
        self.play_is = True
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22)) # отрисовка цветов влево вверху (квадратики)

                text = fontUI.render(str(obj.rank), 1, 'black') # отображение уровней
                rect = text.get_rect(center = (5 + i * 70 + 11, 5 + 11)) # позиция где будут находиться уровни (координаты)
                window.blit(text, rect) # объект который нужно показать, координаты

                text = fontUI.render(str(obj.hp), 1, obj.color) # отображение жизней
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11)) # позиция где будут находиться жизни (координаты)

                window.blit(text, rect) # объект который нужно показать, координаты
                i += 1
                

class Tank:
    def __init__(self, color, px, py, direct, keyList): # Цвета, позиции, направление, список управляющих кнопок
        objects.append(self) # Добавление танка из списка
        self.type = 'tank' # Наименование

        # Сохранение цветов, позиций, направлений
        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = 5 # Кол-во жизни танков
        self.shotTimer = 0 # Время с момента выстрела

        self.moveSpeed = 2 # скорость движения танков
        self.shotDelay = 60 # Задержка между выстрелами
        self.bulletSpeed = 5 # скорость пуль
        self.bulletDamage = 1 # урон от пуль (изначальный)

        # Назначение кнопок с помощью которых идет управление танком
        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.rank = 0
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90) # отрисовка направление для танков
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self): # введение картинок в игру
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90) # отрисовка направление для танков
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5)) # параметр изменения картинок (уменьшение на 5)
        self.rect = self.image.get_rect(center = self.rect.center)

        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        
        oldX, oldY = self.rect.topleft # проверка на столкновение с блоками (возвращает на старую позицию)

        # движение танков (управление, направление)
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                #print (Столкновение)
                self.rect.topleft = oldX, oldY # проверка на столкновение с блоками (возвращает на старую позицию)
                
            # проверка на выход танков за границы игр.поля по вертикали    
            elif obj == self and (self.rect.y<0 or self.rect.y>HEIGHT-30 ):
                #print('Выход за пределы поля')
                self.rect.topleft = oldX, oldY
            # проверка на выход танков за границы игр.поля по горизонтали    
            elif obj == self and (self.rect.x<0 or self.rect.x>WIDTH-30 ):
                #print('Выход за пределы поля')
                self.rect.topleft = oldX, oldY
            
            if obj != self and obj.type == 'tank' and self.rect.colliderect(obj.rect):
                print('Столкновение танков!')
                self.rect.topleft = oldX, oldY
                


        if keys[self.keySHOT] and self.shotTimer == 0:
            # Скорость пуль (реализация)
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage) # Механизм выпускания пуль
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1 # 2 выстрел не будет возможным, пока shotTimer не будет снова равен 0 (Реализация задержки)

    def draw(self):
        window.blit(self.image, self.rect) # Отображение танка

    def damage(self, value):
        self.hp -= value
        # уничтожение одного из танков
        if self.hp <= 0:
            objects.remove(self)
            print(self.color, 'dead')
            if self.color=='blue':
                line1 = "Красный танк победил(синий проиграл)Нажмите на любую клавишу мыши-выход в меню"
            else:
                line1 = "Синий танк победил(красный проиграл)Нажмите на любую клавишу мыши-выход в меню"
            end_fnt = pygame.font.Font(None, 23) # Размер текста
            stroka = end_fnt.render(line1,1,white) # Цвет текста
            print(ui.play_is)
            
            nadpis_= True
            while nadpis_:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()   # sys.exit()
                # при нажатии любой клавиши мыши - цикл
                # while заканчивается и возврат в меню
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        nadpis_ = False
                       
                window.blit(stroka,(120,10))
                pygame.display.flip()
            
            #play = False
            ui.play_is = False
            
        

            

class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage): # Кто из танков выпустил пулю, координаты пули, направление пули, урон
        bullets.append(self) # добавление пуль из списка

        # Сохранение параметров parent, px, py, dx, dy, damage
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):

        # механика пуль
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self) # Удаление пуль которые вылетели за пределы экрана
        else:
            # Столкновение пуль с другим танком
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.type != 'bonus': # алгоритм который не будет проверять столкновение пули со взрывами
                    if obj.rect.collidepoint(self.px, self.py): # координата столкновения пули
                        obj.damage(self.damage) # урон пули
                        bullets.remove(self) # Удаление пули при попадании
                        Bang(self.px, self.py) # передача позиции (при попадании пули после нее отображается взрыв)
                        break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 3) # Отрисовка пули


class Bang: # класс взрывов (отображение)
    def __init__(self, px, py): #  координаты
        objects.append(self)
        self.type = 'bang'

        # позиция где происходит взрыв
        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.2 # скорость воспроизведения взрыва
        if self.frame >= 3: objects.remove(self) # удаление взрыва

    def draw(self):
        image = imgBangs[int(self.frame)] # картинка взрыва
        rect = image.get_rect(center = (self.px, self.py)) # центр изображения взрыва
        window.blit(image, rect)
    
class Block:
    def __init__(self, px, py, size): # координаты, размер блоков
        objects.append(self) # добавление блоков
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size) #
        self.hp = 1 # здоровье блока

    def update(self):
        pass

    def draw(self): # Отрисовка блоков с помощью картинок
        window.blit(imgBrick, self.rect)

    def damage(self, value): # условие при попадании по блоку и после уничтожение его
        self.hp -= value
        if self.hp <= 0: objects.remove(self)

class Bonus:
    def __init__(self, px, py, bonusNum): # координаты, номер бонусов
        objects.append(self) # добавление бонусов
        self.type = 'bonus'

        self.image = imgBonuses[bonusNum] # картинки бонусов
        self.rect = self.image.get_rect(center = (px, py))
        self.timer = 600 # время до исчезновения бонусов
        self.bonusNum = bonusNum
        
        # проверка на столкновение бонуса с другими объектами
        for obj in objects:
            if obj.type == 'block' and self.rect.colliderect(obj.rect):
                try:
                    objects.remove(self)
                except:
                    self.bonusNum = bonusNum


    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            objects.remove(self) # удаление бонуса после исчезновения


        for obj in objects: # алгоритм присваивания уровней, жизней после взятия определенных бонусов
            if obj.type == 'tank' and self.rect.colliderect(obj.rect):
                if self.bonusNum == 0:
                    if obj.rank < len(imgTanks) - 1:
                        obj.rank += 1
                        objects.remove(self)
                        break
                elif self.bonusNum == 1:
                    obj.hp += 1
                    objects.remove(self)
                    break

    def draw(self): # отрисовка "моргания" бонусов
        if self.timer % 30 < 15:
            window.blit(self.image, self.rect)



# класс для вывода на экран меню, выбора пункта меню
class Menu:
    def __init__(self, punkts = [400, 350, u'Punkt', (250,250,30), (250,30,250)]):
        self.punkts = punkts
    # вывод на экран конкретного пункта меню с номером num_punkt
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                #print(i[0], i[1]-30)
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
                
    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)  # мышь сделать видимой
        punkt = 0
        while done:
            info.fill((0, 100, 200))
            screen.fill((0, 100, 200))
 
            mp = pygame.mouse.get_pos() # нажатие мышкой на пункты
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt =i[5]

            # создание параметров в главном меню
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                       sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                           punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                           punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and (mp[0]>350 and mp[0]<570 and mp[1]>270 and mp[1]<410)  and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        print("Правила игры.")
                        pravila(window)
                    elif punkt == 2:
                        print("Управление.")
                        upravlenie(window)
                    elif punkt == 3:
                        sys.exit()
            window.blit(info, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()
            



bullets = []
objects = []

# Продолжение главного меню

punkts = [(350, 260, u'Начать играть', (11, 0, 77), (250,250,30), 0),
          (350, 300, u'Правила игры', (11, 0, 77), (250,250,30), 1),
          (350, 340, u'Управление', (11, 0, 77), (250,250,30), 2),
          (350, 380, u'Выход', (11, 0, 77), (250,250,30), 3)]
game_=True
while game_:
    window.fill('blue')
    bonusTimer = 180

    # Позиции танков, цвета, назначение клавиш для управления
    Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
    Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER))
    ui = UI()

    for _ in range(60): # Кол-во блоков на игровом поле
        while True:# Деление ширины\высоты экрана на размер блока, затем умножение на TILE = позиция строго выравненная на сеточке экрана
            x = randint(0, WIDTH // TILE - 1) * TILE
            y = randint(1, HEIGHT // TILE - 1) * TILE
            rect = pygame.Rect(x, y, TILE, TILE) # Проверка сталкивания блока с другими объектами
            fined = False
            for obj in objects:
                if rect.colliderect(obj.rect): fined = True

            if not fined: break

        Block(x, y, TILE) # создание блоков, (не сталкиваются с другими)
    
    game = Menu(punkts)
    game.menu()




    play = True
    while play:
        if (not ui.play_is):
            play = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                game_= False

        keys = pygame.key.get_pressed() # Глобальные переменные

        if bonusTimer > 0:
            bonusTimer -= 1
        else:
            Bonus(randint(50, WIDTH - 50), randint(50, HEIGHT - 50), randint(0, len(imgBonuses) - 1))
            bonusTimer = randint(120, 240)

        # Обновление и отрисовка пуль, объектов
        for bullet in bullets: bullet.update()
        for obj in objects: obj.update()
        ui.update()

        window.fill('black') # фон игрового поля
        for bullet in bullets: bullet.draw()
        for obj in objects: obj.draw()
        ui.draw()
        
        pygame.display.update()
        clock.tick(FPS)
        
    bullets = [] # Хранение объектов (пули)
    objects = [] # хранение всех объектов в игре
    
pygame.quit()


