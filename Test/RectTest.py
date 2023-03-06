import pygame
import sys

pygame.init()

size = width, height = 500, 500

White = (255, 255, 255)  # RGB 白色
Black = (0, 0, 0)
# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("Python Demo")

clock = pygame.time.Clock()

rect1 = pygame.Rect(0, 0, 50, 50)
rect1.y = 50

image = pygame.image.load("image/again.png")
image2 = pygame.image.load("image/me1.png")

s = pygame.sprite.Sprite()
s.image = image
s.rect = image.get_rect()

s.rect.topleft=(100,10)
g = pygame.sprite.Group()
g.add(s)

#pygame.time.set_timer(400,2000,0)
pygame.time.set_timer(401,500,0)
pygame.time.set_timer(402,2000,0)
print(rect1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type==400:
        #     g.spritedict.popitem()
        #     print(len(g.spritedict))
        if event.type==401:
            for entity in g:
                entity.kill()
        if event.type==402:
            pygame.time.set_timer(401,0)
    screen.fill(Black)
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    g.draw(screen)
    pygame.display.update()
    clock.tick(30)
