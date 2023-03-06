from typing import Tuple
import pygame
import GameEntry
from Param import EnumEvent, EnumSound,EnumColor
import Data


class Action(list):
    def Invoke(self):
        for action in self:
            action()


class Item(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos

    def SetActive(self):
        pass

    def SetInactive(self):
        pass


class Text(Item):
    font: pygame.font.Font
    color: pygame.Color
    text: str

    def __init__(self, pos, datas: dict,):
        super().__init__(pos)
        if("text" in datas):
            self.text = datas["text"]
        else:
            self.text = ""
        if("color" in datas):
            self.color = datas["color"]
        else:
            self.color = EnumColor.Black.value
        if("font" in datas):
            self.font = GameEntry.GameMain.resourceManager.GetFont(
                datas["font"])
        else:
            self.font = GameEntry.GameMain.resourceManager.GetFont(
                Data.Data.DefaultData.DefaultFont)
        self.Refresh()

    def Refresh(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def SetText(self, text: str):
        self.text = text
        self.Refresh()


class Image(Item):
    def __init__(self, pos, datas: dict):
        super().__init__(pos)
        if("image" in datas):
            self.image = GameEntry.GameMain.resourceManager.GetImage(
                datas["image"])
        else:
            self.image = GameEntry.GameMain.resourceManager.GetImage(
                Data.Data.DefaultData.DefaultButtonImage)
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Button(Image):
    onClick: Action
    onPointerEnter: Action
    onPointerLeave: Action
    text: Text
    hasText=False
    IsPoint=False
    def __init__(self, pos, datas: dict):
        super().__init__(pos, datas)
        if("text" in datas):
            self.text = Text(pos, datas)
            self.hasText=True
        self.onClick = Action()
        self.onPointerEnter = Action()
        self.onPointerLeave = Action()

    def SetActive(self):
        self.Register()
        if(self.hasText):
            self.groups()[0].add(self.text)

    def SetInactive(self):
        self.Unregister()

    def Register(self):
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.MouseMotion, self._PointCheck)
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.MouseBtnDown, self._ClickCheck)

    def Unregister(self):
        GameEntry.GameMain.eventManager.Unregister(
            EnumEvent.MouseMotion, self._PointCheck)
        GameEntry.GameMain.eventManager.Unregister(
            EnumEvent.MouseBtnDown, self._ClickCheck)

    def _PointCheck(self, event: pygame.event.Event):
        if(self.rect.collidepoint(event.pos)):
            if(self.IsPoint == True):return
            GameEntry.GameMain.resourceManager.GetSound(
                Data.Data.DefaultData.SoundDic[EnumSound.ButtonPoint]).play()
            self.onPointerEnter.Invoke()
            self.IsPoint = True
        else:
            if(self.IsPoint == False):return
            self.onPointerLeave.Invoke()
            self.IsPoint = False

    def _ClickCheck(self, event: pygame.event.Event):
        if(self.rect.collidepoint(event.pos)):
            GameEntry.GameMain.resourceManager.GetSound(
                Data.Data.DefaultData.SoundDic[EnumSound.ButtonClick]).play()
            self.onClick.Invoke()
