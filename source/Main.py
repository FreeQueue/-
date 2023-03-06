# main.py
import pygame
import sys
from GameEntry import GameMain
from Param import EnumEvent


def Exit(event):
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("飞机大战 -- 112000822孔维焜")
    GameMain.Init()
    GameMain.eventManager.Register(EnumEvent.Quit,Exit)
    clock = pygame.time.Clock()
    while True:
        GameMain.Update()
        clock.tick(60)


if __name__ == '__main__':
    main()
