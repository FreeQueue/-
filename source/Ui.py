from DataBase import UiData, UiItemData
import GameEntry
import pygame
from UiItem import Button, Text
import re
import Data

from Param import EnumEvent, EnumUi


def BuildItem(data: UiItemData):
    item = Data.DefaultData.UiItemDic[data.type](data.pos, data.datas)
    return item


def Match(line: str):
    if(re.match("btn_", line)):
        return True
    if(re.match("txt_", line)):
        return True
    if(re.match("img_", line)):
        return True
    return False


class UiBase():
    ItemDic: dict
    Group: pygame.sprite.Group

    def __init__(self, data: UiData):
        self.ItemDic = dict()
        self.Group = pygame.sprite.Group()
        for item in data.ItemDic:
            self.ItemDic[item] = BuildItem(data.ItemDic[item])
            self.TryBind(item)

    def TryBind(self, item: str):
        if(Match(item)):
            self.__dict__[item] = self.ItemDic[item]

    def Open(self):
        for item in self.ItemDic:
            self.Group.add(self.ItemDic[item])
            self.ItemDic[item].SetActive()

    def Update(self):
        self.Group.draw(GameEntry.GameMain.uiManager.Screen)

    def Close(self):
        for item in self.ItemDic:
           self.ItemDic[item].SetInactive()
        self.Group.empty()


class UiStart(UiBase):
    btn_Start: Button
    btn_Menu: Button
    btn_Exit: Button

    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Start.onClick.append(self.StartGame)
        self.btn_Menu.onClick.append(self.OpenMenu)
        self.btn_Exit.onClick.append(
            lambda: GameEntry.GameMain.eventManager.Fire(EnumEvent.Quit))

    def StartGame(self):
        GameEntry.GameMain.eventManager.Fire(EnumEvent.GameStart)

    def OpenMenu(self):
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiPause)


class UiPause(UiBase):
    btn_Help: Button
    btn_Back: Button

    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Help.onClick.append(lambda: GameEntry.GameMain.uiManager.BackLast())
        self.btn_Back.onClick.append(self.Back)

    def Open(self):
        super().Open()
        GameEntry.GameMain.eventManager.Fire(EnumEvent.GamePause)
    def Back(self):
        GameEntry.GameMain.levelManager.EndLevel()
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiStart)

class UiGame(UiBase):
    btn_Pause: Button
    txt_Score: Text
    txt_Life: Text
    txt_Bomb: Text
    txt_Level: Text
    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Pause.onClick.append(self.Pause)

    def Open(self):
        super().Open()
        GameEntry.GameMain.eventManager.Fire(EnumEvent.GameResume)
        self.txt_Level.SetText("Lv:"+str(GameEntry.GameMain.dataManager.userData.Level))
    def Update(self):
        super().Update()
        self.txt_Score.SetText(str(GameEntry.GameMain.dataManager.runData.Score))
        self.txt_Life.SetText(str(GameEntry.GameMain.levelManager.player.Health))
        self.txt_Bomb.SetText(str(GameEntry.GameMain.dataManager.runData.Bomb))

    def Pause(self):
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiPause)


class UiGameOver(UiBase):
    btn_Restart:Button
    btn_Back:Button
    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Restart.onClick.append(lambda:GameEntry.GameMain.eventManager.Fire(EnumEvent.GameStart))
        self.btn_Back.onClick.append(lambda:GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiStart))    


class UiGameSuccess(UiBase):
    btn_Next:Button
    btn_Back:Button
    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Next.onClick.append(lambda:GameEntry.GameMain.eventManager.Fire(EnumEvent.GameStart))
        self.btn_Back.onClick.append(lambda:GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiStart))   

class UiEnd(UiBase):
    btn_Back:Button
    def __init__(self, data: UiData):
        super().__init__(data)
        self.btn_Back.onClick.append(lambda:GameEntry.GameMain.uiManager.OpenUi(EnumUi.UiStart))
        self.btn_Back.onClick.append(GameEntry.GameMain.dataManager.ResetAllUser())