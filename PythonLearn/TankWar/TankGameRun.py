import pygame
import time
import random

class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 1200
    SCRENN_HEIGHT = 600
    COLOR_BLACK = pygame.Color(0,0,0)
    COLOR_RED = pygame.Color(255,0,0)
    TANL_P1 = None
    ENEMY_TANK_LIST = []
    ENEMY_TANK_NUM = 3
    BULLET_LIST = []
    def __init__(self):
        pass

    def startGame(self):
        pygame.display.init()
        #创建窗口加载窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCRENN_HEIGHT])
        #创建我方坦克
        MainGame.TANL_P1 = Tank(250,300)
        #创建敌方坦克
        self.createEnemyTank()
        #设置游戏标题
        pygame.display.set_caption("Tank War")
        # 让窗口持续刷新
        while True:
            # 填充窗口颜色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            # 获取事件
            self.getEvent()
            # 将绘制文字的小画布沾到窗口
            MainGame.window.blit(self.getTextSurface("敌方剩余坦克%s" % len(MainGame.ENEMY_TANK_LIST)), (5, 5))
            # 画坦克
            MainGame.TANL_P1.dislpayTank()
            for eTank in MainGame.ENEMY_TANK_LIST:
                eTank.dislpayTank()
                eTank.randMove()
            # 画子弹
            for bullet in MainGame.BULLET_LIST:
                bullet.displayBullet()
                bullet.move()


            if not MainGame.TANL_P1.stop:
                MainGame.TANL_P1.move()
            time.sleep(0.02)
            # 窗口更新
            pygame.display.update()
    #获取程序期间所有的事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        #对事件进行判断处理
        for event in eventList:
            # 是否是推出
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按下
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left run")
                    MainGame.TANL_P1.direction = 'L'
                    MainGame.TANL_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print("right run")
                    MainGame.TANL_P1.direction = 'R'
                    MainGame.TANL_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print("down run")
                    MainGame.TANL_P1.direction = 'D'
                    MainGame.TANL_P1.stop = False
                elif event.key == pygame.K_UP:
                    print("up run")
                    MainGame.TANL_P1.direction = 'U'
                    MainGame.TANL_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print("shot")
                    MainGame.BULLET_LIST.append(Bullet(MainGame.TANL_P1))
                else:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.TANL_P1.stop = True
    # 左上角绘制文字neirong
    def getTextSurface(self, text):
        # 字体初始化
        pygame.font.init()
        # 选中合适的字体
        font = pygame.font.SysFont("simsong", 18)
        # 绘制，返回小画布
        textSurface = font.render(text, True, MainGame.COLOR_RED)
        return textSurface

    def createEnemyTank(self):
        for i in range(MainGame.ENEMY_TANK_NUM):
            MainGame.ENEMY_TANK_LIST.append(EnemyTank(random.randint(1,MainGame.SCREEN_WIDTH),100,random.randint(3,6)))

    def endGame(self):
        print("Bye")
        exit()

class Tank():
    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load('imgs/p1tankU.gif'),
            'D': pygame.image.load('imgs/p1tankD.gif'),
            'R': pygame.image.load('imgs/p1tankR.gif'),
            'L': pygame.image.load('imgs/p1tankL.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop = True
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCRENN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        else:
            pass

    def shot(self):
        return Bullet(self)

    def dislpayTank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image, self.rect)

class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        self.images = {
            'U': pygame.image.load('imgs/enemy1U.gif'),
            'D': pygame.image.load('imgs/enemy1D.gif'),
            'R': pygame.image.load('imgs/enemy1R.gif'),
            'L': pygame.image.load('imgs/enemy1L.gif')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.step = 50

    def randDirection(self):
        return random.choice(['U', 'D', 'L', 'R'])

    def randMove(self):
        if self.step <=0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1
class Bullet():
    def __init__(self, tank):
        self.image = pygame.image.load('imgs/tankmissile.gif')
        self.direction = tank.direction
        self.speed = MainGame.TANL_P1.speed * 1.5
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        else:
            pass

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCRENN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        else:
            pass
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)

class Explode():
    def __init__(self):
        pass
    def displayExplode(self):
        pass

class Wall():
    def __init__(self):
        pass
    def displayWall(self):
        pass

class Music():
    def __init__(self):
        pass
    def play(self):
        pass

if __name__ == '__main__':
    MainGame().startGame()