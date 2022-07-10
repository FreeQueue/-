from enum import Enum, IntEnum
import pygame


class EnumImage(IntEnum):
    Background = 0
    Again = 1
    GameOver = 2
    Pause = 3
    Resume = 4
    Life = 51
    Bomb = 52

    Player = 100
    PlayerDown1 = 101
    PlayerDown2 = 102
    PlayerDown3 = 103
    PlayerDown4 = 104
    Enemy1 = 200
    Enemy1Down1 = 201
    Enemy1Down2 = 202
    Enemy1Down3 = 203
    Enemy1Down4 = 204
    Enemy2 = 300
    Enemy2Down1 = 301
    Enemy2Down2 = 302
    Enemy2Down3 = 303
    Enemy2Down4 = 304
    Boss = 400
    BossDown1 = 401
    BossDown2 = 402
    BossDown3 = 403
    BossDown4 = 404
    BossDown5 = 405
    BossDown6 = 406
    PlayerBullet = 500
    EnemyBullet = 501
    BombSupply = 502
    BulletSupply = 503


class EnumSound(IntEnum):
    ButtonPoint = 1
    ButtonClick = 2
    PlayerDestroy = 3
    Enemy1Destroy = 4
    Enemy2Destroy = 5
    BossDestroy = 6
    BossFly = 7
    GetBomb = 8
    UseBomb = 9
    Upgrade = 10


class EnumColor(Enum):
    White = (255, 255, 255)
    Black = (0, 0, 0)


class EnumUiItem(IntEnum):
    Image = 1
    Button = 2
    Text = 3


class EnumUi(IntEnum):
    UiStart = 0
    GameUi = 1
    UiPause = 2
    GameOverUi = 3
    GameSuccessUi = 4
    GameEnd = 5


class EnumGroup(IntEnum):
    Player = 1
    Enemies = 2
    Supply = 3
    Other = 4


class EnumEntity(IntEnum):
    Player = 0
    Enemy1 = 1
    Enemy2 = 2
    PlayerBullet = 3
    EnemyBullet = 4
    Boss = 5
    BombSupply = 6


class EnumEvent(IntEnum):
    Quit = pygame.QUIT
    MouseMotion = pygame.MOUSEMOTION
    MouseBtnDown = pygame.MOUSEBUTTONDOWN
    GameStart = pygame.USEREVENT
    GamePause = pygame.USEREVENT+1
    GameResume = pygame.USEREVENT+2
    GameOver = pygame.USEREVENT+3
    GameFinish = pygame.USEREVENT+4
    Supply = pygame.USEREVENT+5


class Decs(IntEnum):
    Double = 1
    Triple = 2
    Circle = 3
    Offset = 4
    Sleep = 0


class GenBulletParam():
    type: EnumEntity
    pos: pygame.Vector2
    speed: pygame.Vector2

    def __init__(self, type: EnumEntity, position: pygame.Vector2, speed: pygame.Vector2):
        self.type = type
        self.pos = position
        self.speed = speed
