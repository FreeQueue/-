from typing import Tuple
import pygame
import GameEntry
from Data import DefaultData, RunData,UserData
from Param import EnumGroup, EnumUi, EnumColor, EnumEvent, EnumEntity, EnumImage
from Ui import UiBase
from Entity import EntityBase, PlayerEntity
from Generator import EnemyGenerator, SupplyGenerator

class ManagerBase():
    def __init__(self):
        GameEntry.GameMain.Register(self)

    def Update(self):
        pass


class ResourceManager(ManagerBase):
    _SoundDic: dict
    _ImageDic: dict
    _FontDic: dict

    def __init__(self):
        super().__init__()
        self._SoundDic = dict()
        self._ImageDic = dict()
        self._FontDic = dict()

    def GetImage(self, path: str) -> pygame.Surface:
        if(path in self._ImageDic.keys()):
            return self._ImageDic[path]
        else:
            image = pygame.image.load(
                DefaultData.ImageRoot + path).convert_alpha()
            self._ImageDic[path] = image
            return image

    def GetSound(self, path: str) -> pygame.mixer.Sound:
        if(path in self._SoundDic.keys()):
            return self._SoundDic[path]
        else:
            sound = pygame.mixer.Sound(DefaultData.SoundRoot + path)
            self._SoundDic[path] = sound
            return sound

    def GetFont(self, path: str, size: int = 48) -> pygame.font.Font:
        if(path in self._FontDic.keys()):
            return self._FontDic[path]
        else:
            font = pygame.font.Font(DefaultData.FontRoot + path, size)
            self._FontDic[path] = font
            return font


class DataManager(ManagerBase):
    runData: RunData
    userData: UserData

    def __init__(self):
        super().__init__()
        self.runData = RunData()
        self.userData = UserData()

    def ResetAllRun(self):
        self.runData = RunData()

    def ResetAllUser(self):
        self.userData=UserData()
    
    def ResetRunData(self, dataName: str):
        self.runData.__dict__[dataName] = RunData.__dict__[dataName]

    def ResetUserData(self, dataName: str):
        self.userData.__dict__[dataName] = UserData.__dict__[dataName]


class EventManager(ManagerBase):
    _EventDic: dict

    def __init__(self):
        super().__init__()
        self._EventDic = dict()

    def Update(self):
        for event in pygame.event.get():
            if(event.type in self._EventDic.keys()):
                for func in self._EventDic[event.type]:
                    func(event)

    def Register(self, eventType: EnumEvent, func):
        if(eventType not in self._EventDic):
            self._EventDic[eventType] = []
            print("event:{} make".format(eventType.name))
        if(func in self._EventDic[eventType]):
            print("Func:{} has registered".format(func))
            return
        self._EventDic[eventType].append(func)

    def Unregister(self, eventType: EnumEvent, func):
        if(eventType not in self._EventDic):
            print("event:{} is invalid".format(eventType.name))
            return
        if(func not in self._EventDic[eventType]):
            print("Func:{} has no registered".format(func))
            return
        self._EventDic[eventType].remove(func)

    def Fire(self, event: int, time: int = 1, loops: int = 1):
        pygame.time.set_timer(event, time, loops)

    def EndFire(self, event: int):
        pygame.time.set_timer(event, 0)

    def ClearEvent(self, event: int):
        self._EventDic[event].clear()

    def Clear(self):
        self._EventDic.clear()
# pygame.sprite.Group().


class EntityManager(ManagerBase):
    _Groups: dict
    _EntityPool: dict

    def __init__(self):
        super().__init__()
        self._Groups = {}
        self._EntityPool = {}
        for enum in EnumEntity:
            self._EntityPool[enum] = pygame.sprite.Group()
        for enum in EnumGroup:
            self._Groups[enum] = pygame.sprite.Group()

    def Update(self):
        super().Update()
        if(GameEntry.GameMain.levelManager.InGame == False):
            return
        for group in self._Groups:
            self._Groups[group].update()

    def Draw(self):
        for group in self._Groups:
            self._Groups[group].draw(GameEntry.GameMain.uiManager.Screen)

    def ShowEntity(self, enum: EnumEntity, pos: Tuple[int, int]) -> EntityBase:
        entities = self._EntityPool[enum].spritedict
        entity: EntityBase
        if(len(entities) > 0):
            entity = entities.popitem()[0]
        else:
            entity = DefaultData.EntityDic[enum](
                DefaultData.EntityDataDic[enum])
            entity.Type = enum
        self._Groups[entity.CollideGroup].add(entity)
        entity.rect.center = pos
        entity.OnShow()
        return entity

    def GetGroup(self, group: EnumGroup) -> pygame.sprite.Group:
        return self._Groups[group]

    def HideEntity(self, entity: EntityBase):
        entity.OnHide()
        self._Groups[entity.CollideGroup].remove(entity)
        self._EntityPool[entity.Type].add(entity)

    def ClearGroup(self, enum: EnumGroup):
        for entity in self._Groups[enum]:
            self._Groups[enum].remove(entity)
            self._EntityPool[entity.Type].add(entity)

    def ClearAll(self):
        for enum in EnumGroup:
            self.ClearGroup(enum)


class UiManager(ManagerBase):
    Screen: pygame.Surface
    ScreenRect: pygame.Rect
    currentUi: UiBase
    lastUi: UiBase
    UiDic: dict

    def __init__(self):
        super().__init__()
        self.UiDic = dict()
        self.Screen = pygame.display.set_mode(
            DefaultData.ScreenSize)
        self.ScreenRect = self.Screen.get_rect()
        for enum in EnumUi:
            self.UiDic[enum] = DefaultData.UiDic[enum](
                DefaultData.UiDataDic[enum])
        self.currentUi = self.UiDic[EnumUi.UiStart]
        self.currentUi.Open()

    def OpenUi(self, enum: EnumUi):
        self.lastUi = self.currentUi
        self.currentUi.Close()
        self.currentUi = self.UiDic[enum]
        self.currentUi.Open()

    def BackLast(self):
        tmp = self.currentUi
        self.currentUi.Close()
        self.currentUi = self.lastUi
        self.lastUi = tmp
        self.currentUi.Open()

    def Update(self):
        self.Screen.blit(pygame.transform.scale(GameEntry.GameMain.resourceManager.GetImage(
            DefaultData.ImageDic[EnumImage.Background]), DefaultData.ScreenSize), (0, 0))
        if(GameEntry.GameMain.levelManager.InGame):
            GameEntry.GameMain.entityManager.Draw()
        self.currentUi.Update()
        pygame.display.update()


class InputManager(ManagerBase):
    Up = False
    Down = False
    Left = False
    Right = False
    Space = False

    def __init__(self):
        super().__init__()

    def Update(self):
        key_pressed = pygame.key.get_pressed()
        self.Up = key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]
        self.Down = key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]
        self.Left = key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]
        self.Right = key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]
        self.Space = key_pressed[pygame.K_SPACE]


class LevelManager(ManagerBase):
    enemyGenerator: EnemyGenerator
    supplyGenerator: SupplyGenerator
    startTime: int
    InGame = False
    player: PlayerEntity

    def __init__(self):
        super().__init__()
        self.enemyGenerator = EnemyGenerator()
        self.supplyGenerator = SupplyGenerator()
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.GameStart, self.StartLevel)
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.GamePause, self.Pause)
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.GameResume, self.Resume)
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.GameOver, self.LevelFail)
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.GameFinish, self.LevelSuccess)

    def Pause(self, event):
        self.InGame = False

    def Resume(self, event):
        self.InGame = True

    def Update(self):
        super().Update()
        if(self.InGame):
            self.Timer()
            self.enemyGenerator.Update()

    def StartLevel(self, event):
        if(GameEntry.GameMain.dataManager.userData.Level not in DefaultData.LevelDic.keys()):
            GameEntry.GameMain.uiManager.OpenUi(EnumUi.GameEnd)
            return
        self.player = GameEntry.GameMain.entityManager.ShowEntity(
            EnumEntity.Player, (DefaultData.Width/2, DefaultData.Height-50))
        GameEntry.GameMain.eventManager.Fire(EnumEvent.Supply, 10*1000, 0)
        self.enemyGenerator.SetMusic(
            DefaultData.LevelDic[GameEntry.GameMain.dataManager.userData.Level])
        self.startTime = pygame.time.get_ticks()
        self.InGame = True
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.GameUi)

    def EndLevel(self):
        self.InGame = False
        GameEntry.GameMain.dataManager.ResetAllRun()
        GameEntry.GameMain.eventManager.EndFire(EnumEvent.Supply)
        GameEntry.GameMain.entityManager.ClearAll()

    def Timer(self):
        GameEntry.GameMain.dataManager.runData.Time = pygame.time.get_ticks() - \
            self.startTime

    def LevelFail(self, event):
        if(self.InGame == False):
            raise Exception("Invalid Event")
        self.EndLevel()
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.GameOverUi)

    def LevelSuccess(self, event):
        if(self.InGame == False):
            raise Exception("Invalid Event")
        self.EndLevel()
        GameEntry.GameMain.dataManager.userData.Level += 1
        GameEntry.GameMain.uiManager.OpenUi(EnumUi.GameSuccessUi)
