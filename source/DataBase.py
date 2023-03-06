from typing import Tuple

from pygame import Vector2


class EntityDataBase():
    Image: str
    Speed: Vector2

    def __init__(self, imagePath: str, speed: Vector2):
        self.Image = imagePath
        self.Speed = speed


class BulletData(EntityDataBase):
    HitGroup: str
    Damage: int

    def __init__(self, hitGroup: str, imagePath: str, speed: Vector2, damage: int = 1):
        super().__init__(imagePath, speed)
        self.HitGroup = hitGroup
        self.Damage = damage


class EnemyData(EntityDataBase):
    OriginHealth: int
    '初始生命值'
    DestroyImages: list
    '摧毁动画图集路径'
    DestroySound: str
    '摧毁音效'
    BulletMusic: list
    Score:int
    def __init__(self,score:int ,imagePath: str,speed: Vector2, originHealth: int, destroyImages: list, bulletMusic: list, bulletParam, destroySound: str):
        super().__init__(imagePath,speed)
        self.Score=score
        self.DestroyImages = destroyImages
        self.BulletMusic = bulletMusic
        self.OriginHealth = originHealth
        self.DestroySound = destroySound
        self.BulletParam = bulletParam


class PlayerData(EnemyData):
    pass


class UiItemData():
    # type:Param.EnumUiItem
    pos: Tuple[int, int]
    datas: dict

    def __init__(self, type, pos: Tuple[int, int], datas: dict):
        self.type = type
        self.datas = datas
        self.pos = pos


class UiData():
    ItemDic: dict

    def __init__(self, *args: Tuple[str, UiItemData]):
        self.ItemDic = dict()
        for i in args:
            self.ItemDic[i[0]] = i[1]
