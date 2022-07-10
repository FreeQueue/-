from pygame import Vector2
from UiItem import *
from DataBase import *
from Param import *
from Ui import *
from Entity import *


class DefaultData():
    ImageRoot = "image/"
    SoundRoot = "sound/"
    FontRoot = "font/"
    DefaultFont = "font.ttf"
    ScreenSize = Width, Height = 500, 900

    ImageDic = {
        EnumImage.PlayerBullet: "bullet1.png",
        EnumImage.EnemyBullet: "bullet2.png",
        EnumImage.Background: "background.png",
        EnumImage.Again: "again.png",
        EnumImage.GameOver: "gameover.png",
        EnumImage.Pause: "pause_nor.png",
        EnumImage.Resume: "resume_nor.png",
        EnumImage.Life: "life.png",
        EnumImage.Bomb: "bomb.png",
        EnumImage.Player: "me1.png",
        EnumImage.PlayerDown1: "me_destroy_1.png",
        EnumImage.PlayerDown2: "me_destroy_2.png",
        EnumImage.PlayerDown3: "me_destroy_3.png",
        EnumImage.PlayerDown4: "me_destroy_4.png",
        EnumImage.Enemy1: "enemy1.png",
        EnumImage.Enemy1Down1: "enemy1_down1.png",
        EnumImage.Enemy1Down2: "enemy1_down2.png",
        EnumImage.Enemy1Down3: "enemy1_down3.png",
        EnumImage.Enemy1Down4: "enemy1_down4.png",
        EnumImage.Enemy2: "enemy2.png",
        EnumImage.Enemy2Down1: "enemy2_down1.png",
        EnumImage.Enemy2Down2: "enemy2_down2.png",
        EnumImage.Enemy2Down4: "enemy2_down4.png",
        EnumImage.Enemy2Down3: "enemy2_down3.png",
        EnumImage.Boss: "enemy3_n1.png",
        EnumImage.BossDown1: "enemy3_down1.png",
        EnumImage.BossDown2: "enemy3_down2.png",
        EnumImage.BossDown3: "enemy3_down3.png",
        EnumImage.BossDown4: "enemy3_down4.png",
        EnumImage.BossDown5: "enemy3_down5.png",
        EnumImage.BossDown6: "enemy3_down6.png",
        EnumImage.PlayerBullet: "bullet1.png",
        EnumImage.EnemyBullet: "bullet2.png",
        EnumImage.BombSupply: "bomb_supply.png",
        EnumImage.BulletSupply: "bullet_supply.png",
    }
    SoundDic = {
        EnumSound.ButtonPoint: "button.wav",
        EnumSound.ButtonClick: "button.wav",
        EnumSound.PlayerDestroy: "me_down.wav",
        EnumSound.Enemy1Destroy: "enemy1_down.wav",
        EnumSound.Enemy2Destroy: "enemy2_down.wav",
        EnumSound.BossDestroy: "enemy3_down.wav",
        EnumSound.BossFly: "enemy3_flying.wav",
        EnumSound.GetBomb: "get_bomb.wav",
        EnumSound.UseBomb: "use_bomb.wav",
        EnumSound.Upgrade: "upgrade.wav",
    }

    PlayerBulletMusic = [(Decs.Sleep, 20)]
    Enemy1BulletMusic = [(Decs.Sleep, 100)]
    Enemy2BulletMusic = [(Decs.Sleep, 100)]
    BossBulletMusic = [(Decs.Sleep, 20)]
    DefaultBulletPos = Vector2(0, 1)
    PlayerBulletSpeed = Vector2(0, -5)
    EnemyBulletSpeed = Vector2(0, 5)
    PlayerBulletData = BulletData(
        EnumGroup.Enemies, ImageDic[EnumImage.PlayerBullet], (0, -5))
    EnemyBulletData = BulletData(
        EnumGroup.Player, ImageDic[EnumImage.EnemyBullet], (0, 5))
    PlayerBulletParam = GenBulletParam(
        EnumEntity.PlayerBullet, DefaultBulletPos, PlayerBulletSpeed)
    Enemy1BulletParam = GenBulletParam(
        EnumEntity.EnemyBullet, DefaultBulletPos, EnemyBulletSpeed)
    Enemy2BulletParam = GenBulletParam(
        EnumEntity.EnemyBullet, DefaultBulletPos, EnemyBulletSpeed)
    BossBulletParam = GenBulletParam(
        EnumEntity.EnemyBullet, DefaultBulletPos, EnemyBulletSpeed)
    EntityDic = {
        EnumEntity.Player: PlayerEntity,
        EnumEntity.Enemy1: EnemyEntity,
        EnumEntity.Enemy2: EnemyEntity,
        EnumEntity.Boss: Boss,
        EnumEntity.BombSupply: SupplyEntity,
        EnumEntity.PlayerBullet: BulletEntity,
        EnumEntity.EnemyBullet: BulletEntity,
    }
    EntityDataDic = {
        EnumEntity.Player: PlayerData(0, ImageDic[EnumImage.Player], Vector2(0, 0), 10, [ImageDic[EnumImage.Player], ImageDic[EnumImage.Player], ImageDic[EnumImage.Player], ImageDic[EnumImage.Player]], PlayerBulletMusic, PlayerBulletParam, SoundDic[EnumSound.PlayerDestroy]),
        EnumEntity.Enemy1: EnemyData(100, ImageDic[EnumImage.Enemy1], Vector2(0, 1), 3, [ImageDic[EnumImage.Enemy1Down1], ImageDic[EnumImage.Enemy1Down2], ImageDic[EnumImage.Enemy1Down3], ImageDic[EnumImage.Enemy1Down4]], Enemy1BulletMusic, Enemy1BulletParam, SoundDic[EnumSound.Enemy1Destroy]),
        EnumEntity.Enemy2: EnemyData(200, ImageDic[EnumImage.Enemy2], Vector2(0, 1), 6, [ImageDic[EnumImage.Enemy2Down1], ImageDic[EnumImage.Enemy2Down2], ImageDic[EnumImage.Enemy2Down3], ImageDic[EnumImage.Enemy2Down4]], Enemy2BulletMusic, Enemy2BulletParam, SoundDic[EnumSound.Enemy2Destroy]),
        EnumEntity.Boss: EnemyData(1000, ImageDic[EnumImage.Boss], Vector2(0, 0), 30, [ImageDic[EnumImage.BossDown1], ImageDic[EnumImage.BossDown2], ImageDic[EnumImage.BossDown3], ImageDic[EnumImage.BossDown4], ImageDic[EnumImage.BossDown5], ImageDic[EnumImage.BossDown6]], BossBulletMusic, BossBulletParam, SoundDic[EnumSound.BossDestroy]),
        EnumEntity.BombSupply: EntityDataBase(ImageDic[EnumImage.BombSupply], Vector2(0, 3)),
        EnumEntity.PlayerBullet: PlayerBulletData,
        EnumEntity.EnemyBullet: EnemyBulletData,
    }
    UiDic = {
        EnumUi.UiStart: UiStart,
        EnumUi.UiPause: UiPause,
        EnumUi.GameUi: UiGame,
        EnumUi.GameSuccessUi: UiGameSuccess,
        EnumUi.GameOverUi: UiGameOver,
        EnumUi.GameEnd: UiEnd, }
    UiDataDic = {
        EnumUi.UiStart: UiData(("btn_Start", UiItemData(EnumUiItem.Button, (Width/2, 200), {"text": "Start", })),
                               ("btn_Menu", UiItemData(EnumUiItem.Button,
                                (Width/2, 400), {"text": "Menu", })),
                               ("btn_Exit", UiItemData(EnumUiItem.Button, (Width/2, 600), {"text": "Exit", }))),
        EnumUi.UiPause: UiData(("btn_Help", UiItemData(EnumUiItem.Button, (Width/2, 200), {"text": "Resume", })),
                               ("btn_Back", UiItemData(EnumUiItem.Button, (Width/2, 400), {"text": "BackMenu", })),),
        EnumUi.GameUi: UiData(("btn_Pause", UiItemData(EnumUiItem.Button, (Width-50, 50), {"image": ImageDic[EnumImage.Pause]})),
                              ("bomb", UiItemData(EnumUiItem.Image, (Width-50,
                               Height-50), {"image": ImageDic[EnumImage.Bomb], })),
                              ("life", UiItemData(
                                  EnumUiItem.Image, (50, Height-50), {"image": ImageDic[EnumImage.Life], })),
                              ("txt_Level", UiItemData(
                                  EnumUiItem.Text, (Width-150, 50), {})),
                              ("txt_Score", UiItemData(
                                  EnumUiItem.Text, (50, 50), {})),
                              ("txt_Bomb", UiItemData(
                                  EnumUiItem.Text, (Width-100, Height-50), {})),
                              ("txt_Life", UiItemData(EnumUiItem.Text, (100, Height-50), {})),),
        EnumUi.GameOverUi: UiData(("btn_Restart", UiItemData(EnumUiItem.Button, (Width/2, 200), {"text": "Restart", })),
                                  ("btn_Back", UiItemData(EnumUiItem.Button, (Width/2, 400), {"text": "BackMenu", })),),
        EnumUi.GameSuccessUi: UiData(("btn_Next", UiItemData(EnumUiItem.Button, (Width/2, 200), {"text": "Next", })),
                                     ("btn_Back", UiItemData(EnumUiItem.Button, (Width/2, 400), {"text": "BackMenu", })),),
        EnumUi.GameEnd: UiData(("End", UiItemData(EnumUiItem.Text, (Width/2, 200), {"text": "The End", })),
                               ("Thanks", UiItemData(EnumUiItem.Text,
                                (Width/2, 400), {"text": "Thanks for play", })),
                               ("btn_Back", UiItemData(EnumUiItem.Button, (Width/2, 600), {"text": "BackMenu", })),), }

    UiItemDic = {
        EnumUiItem.Image: Image,
        EnumUiItem.Button: Button,
        EnumUiItem.Text: Text,
    }
    EnemyMusic1 = {
        0: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        3000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        6000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        8000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        12000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        12000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        14000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        16000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        20000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        22000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        23000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        25000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        26000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        27000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        30000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        35000: (EnumEntity.Boss, (random.randint(30, Width-30), 0)),
    }
    EnemyMusic2 = {
        0: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        3000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        6000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        8000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        12000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        12000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        14000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        16000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        20000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        22000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        23000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        25000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        26000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        27000: (EnumEntity.Enemy1, (random.randint(30, Width-30), 0)),
        30000: (EnumEntity.Enemy2, (random.randint(30, Width-30), 0)),
        35000: (EnumEntity.Boss, (random.randint(30, Width-30), 0)),
    }
    LevelDic = {
        1: EnemyMusic1,
        2: EnemyMusic2,
    }
    DefaultButtonImage = ImageDic[EnumImage.Again]
    DefaultPlayerSpeed = 5


class RunData():
    Score = 0
    '分数'
    Bomb = 3
    '炸弹数'
    Time = 0
    Buff: list

    def __init__(self):
        self.Buff = list()

class UserData():
    Level = 1
    def __init__(self):
        pass
    def ResetAll():
        pass