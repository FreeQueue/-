import pygame
import sys
class Action(list):
    def Invoke(self):
        for action in self:
            action()

class Button(pygame.sprite.Sprite):
    onClick:Action
    onPointerEnter:Action
    onPointerLeave:Action
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.onClick=Action()
        self.onPointerEnter=Action()
        self.onPointerLeave=Action()
    def PointCheck(self,event:pygame.event.Event):
        if(self.rect.collidepoint(event.pos)):
            self.IsPoint=True
            self.onPointerEnter.Invoke()
        else:
            self.IsPoint=False
            self.onPointerLeave.Invoke()
    def ClickCheck(self,event:pygame.event.Event):
        if(self.rect.collidepoint(event.pos)):
            self.onClick.Invoke()


pygame.init()

size = width, height = 500, 500

White = (255, 255, 255)  # RGB 白色
Black = (0, 0, 0)
# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("Python Demo")

clock = pygame.time.Clock()


image = pygame.image.load("image/again.png")
image2 = pygame.image.load("image/me1.png")

class A():
    def __init__(self):
        self. s = Button()
        self.s.image = image
        #self.s.rect = image.get_rect()
        self.s.onClick.append(self.pp)
    def pp(self):
        print(self)
a=A()
g = pygame.sprite.Group()
g.add(a.s)
pygame.time.set_timer(400,2000,1)
pygame.time.set_timer(401,3000,1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            a.s.ClickCheck(event)
    screen.fill(Black)
    g.draw(screen)
    pygame.display.update()
    clock.tick(30)
