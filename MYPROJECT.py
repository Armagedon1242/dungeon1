import pygame
import random
import S
import time
pygame.init()
#экран и др--------------------------------------------------------------------------------------------------------
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#------------------------------------------------------------------------------------------------------------------
walls = []
ghosts = []
xx = 260
yy = 260
spell = 1
sss = 0
S.changecolor('y')
print('В этой игре можно двигать всё (если приловчиться). Но не следует переувлекаться, ведь каждый раз КОНЕЦ удаляется!')
print('1 это удар, 2 это лечение (переключение цифрами) (нажмите пробел).')
S.changecolor('black')
f1 = pygame.font.Font(None, 36)
text1 = f1.render('HP', 1, (255, 255, 255))
text2 = f1.render('MP', 1, (255, 255, 255))
text3 = f1.render(str(spell), 1, (255, 255, 255))
f = 0
class Obj:
    def __init__(self, x, y, w, h, img,speed,type):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.type = type
        self.speedd = speed
        self.f = 0
        if self.type == 'ghost':
            ghosts.append(self) 
    def attack(self):
        if player.rect.x > self.rect.x:
            if player.rect.x - self.rect.x < 200:
                self.rect.x += 1
        if player.rect.y > self.rect.y:
            if player.rect.y - self.rect.y < 200:
                self.rect.y += 1
        if player.rect.x < self.rect.x:
            if self.rect.x - player.rect.x < 200:
                self.rect.x -= 1
        if player.rect.y < self.rect.x:
            if self.rect.x - player.rect.x < 200:
                self.rect.y -= 1
        if self.rect.x == player.rect.x or self.rect.y == player.rect.y:
            self.rect.y -= 1
            self.rect.x -= 1
    def collide(self, obj):
        return self.rect.colliderect(obj.rect) 
    def death(self):
        if self.type == 'ghost' and self.rect.colliderect(a):
            self.rect.x += 10000
            ghosts.remove(self)
        if self.type == 'boss' and self.rect.colliderect(a):
            self.speedd -= 5 
            if self.speedd < 1:
                self.rect.x += 10000
                walls.remove(self)  
                S.changecolor('y')
                print('Вот и настал КОНЕЦ.')
                print('''
Благодарности:
EasyCode,
Друзья,
Родители,
Родные,
Наш учитель Сергей,                      
И все-все люди на земле!  
''')
                S.stop(0)             
    def move(self,player):
        self.rect.x -= player.x_speed
        if self.collide(player):
            if self.type == 'lava' or self.type == 'ghost' or self.type == 'boss'or self.type == 'D'or self.type == 'U'or self.type == 'L'or self.type == 'R':
                player.hp -= 0.1
            if self.type == 'boss':
                player.hp -= 0.5
                S.changecolor('r')
                print('Это финал.')
                S.changecolor('c')
            for self in walls:
                self.rect.x += player.x_speed 

        self.rect.y -= player.y_speed
        if self.collide(player):
            if self.type == 'lava' or self.type == 'ghost' or self.type == 'boss'or self.type == 'D'or self.type == 'U'or self.type == 'L'or self.type == 'R':
                player.hp -= 0.1    
            if self.type == 'boss':
                player.hp -= 0.5
                S.changecolor('r')
                print('Это финал.')
                S.changecolor('c')        
            for self in walls:
                self.rect.y += player.y_speed 
    def repeating_move(self):
        
        if self.type == 'D':
            self.f += 1
            if self.f < 150:
                self.rect.y += 1
            if self.f == 150:
                self.rect.y -= 150
                self.f = 0
        if self.type == 'U':
            self.f += 1
            if self.f < 150:
                self.rect.y -= 1
            if self.f == 150:
                self.rect.y += 150
                self.f = 0
        if self.type == 'R':
            self.f += 1
            if self.f < 150:
                self.rect.x += 1
            if self.f == 150:
                self.rect.x -= 150
                self.f = 0
        if self.type == 'L':
            self.f += 1
            if self.f < 150:
                self.rect.x -= 1
            if self.f == 150:
                self.rect.x += 150
                self.f = 0

    def draw(self):
        screen.blit(self.img,self.rect ) 
    
with open("map.txt","r") as map1:
    row, col = 0, 0
    for line in map1.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '2':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'Lava.webp',0,'lava'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'wall.png',0,'wall'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '3':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'ghost.png',0,'ghost'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '4':
                walls.append(Obj(col * 25, row * 25, 50, 75, 'boss3.png',500,'boss'))
            col += 1
        row += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == 'L':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'FLARE.png',0,'L'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == 'R':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'FLARE.png',0,'R'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == 'U':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'FLARE.png',0,'U'))
            col += 1
        row += 1
with open("map.txt","r") as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == 'D':
                walls.append(Obj(col * 25, row * 25, 25, 25, 'FLARE.png',0,'D'))
            col += 1
        row += 1
class Player:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.x_speed = 0
        self.y_speed = 0
        self.hp = 100
        self.mana = 100
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)
    def draw(self):
        screen.blit(self.img, self.rect) 


player = Player(225,225,25,25,'player.png')
while True:
    S.changecolor('c')
    text3 = f1.render(str(spell), 1, (255, 255, 255))
    screen.fill((25,20,15))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            S.stop(0)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                player.y_speed = -5
            elif e.key == pygame.K_DOWN:
                player.y_speed = 5
            elif e.key == pygame.K_LEFT:
                player.x_speed = -5
                player.img = pygame.transform.scale(pygame.image.load('player.png'), (25,25))
            elif e.key == pygame.K_RIGHT:
                player.x_speed = 5
                player.img = pygame.transform.scale(pygame.image.load('playerright.png'), (25,25))
            elif e.key == pygame.K_SPACE:
                if sss == 0:
                    sss = 1
                else:
                    sss = 0
            elif e.key == pygame.K_1:
                if spell != 1:
                    spell = 1
                else:
                    spell = 0
            elif e.key == pygame.K_2:
                if spell != 2:
                    spell = 2
                else:
                    spell = 0

        elif e.type == pygame.KEYUP:
            player.x_speed = 0
            player.y_speed = 0
    for wall in walls:    
        wall.draw()
    if player.hp <= 0:
        S.changecolor('r')
        print('Вот и настал КОНЕЦ.')

        S.stop(0)

    if spell == 1 and player.mana >= 2 and sss == 1:
        a = pygame.draw.rect(screen,(255,255,10),(xx,yy,5,5))
        player.mana -= 2 
        if yy > 210 and xx == 260:
            yy -= 5
        elif yy == 210 and xx > 210:
            xx -= 5
        if xx == 210 and yy < 260:
                yy += 5       
        if yy == 260 and xx < 260:
                xx += 5    
        for w in walls:
            w.death()
    if spell == 2 and player.mana >= 20 and sss == 1:
       player.mana-= 20  
       player.hp += 10
    for wall in walls:
        wall.move(player)
    for wall in walls:
        wall.repeating_move()
    for g in ghosts:
        g.attack()
    for wall in walls:
        if wall.type == 'boss' and wall.speedd <= 0:
           S.changecolor('y')
           print('Вот и настал КОНЕЦ. Хорошая получилась история.')
           S.stop(0)
    player.draw()
    pygame.draw.rect(screen, (255,0,10),(40,10,100,20))
    pygame.draw.rect(screen, (0,255,10),(40,10,player.hp,20))
    screen.blit(text1, (2, 9))
    screen.blit(text3, (2, 69))
    pygame.draw.rect(screen, (20,20,255),(40,40,100,20))
    pygame.draw.rect(screen, (0,150,255),(40,40,player.mana,20))
    screen.blit(text2, (2, 39))
    if player.mana < 100:
        player.mana += 0.5
    if player.hp > 100:
        player.hp = 100   
    if player.mana < 2:
        sss = 0
    pygame.display.update()
    clock.tick(60)