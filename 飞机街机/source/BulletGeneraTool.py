from functools import wraps
from typing import Iterator
from Param import Decs, GenBulletParam
import GameEntry


def DoubleBullet(offset: int = 0):
    def Dec(func):
        @wraps(func)
        def WarpDec(param: GenBulletParam):
            offsetPosition = param.speed.normalize().yx*offset
            param.pos += offsetPosition
            func(param)
            param.pos -= offsetPosition*2
            func(param)
        return WarpDec
    return Dec


def TripleBullet(offset: int = 0):
    def Dec(func):
        @wraps(func)
        def WarpDec(param: GenBulletParam):
            offsetPosition = param.speed.normalize().yx*offset
            func(param)
            param.pos += offsetPosition
            func(param)
            param.pos -= offsetPosition*2
            func(param)
        return WarpDec
    return Dec


def CircleBullet(num: int):
    def Dec(func):
        @wraps(func)
        def WarpDec(param: GenBulletParam):
            rad = 360/num
            for i in range(num):
                param.speed.rotate_ip(rad)
                func(param)
        return WarpDec
    return Dec


def OffsetBullet(offset: int, num: int = 2):
    def Dec(func):
        @wraps(func)
        def WarpDec(param: GenBulletParam):
            for i in range(num):
                param.pos.x += offset
                func(param)
        return WarpDec
    return Dec


def Decorator(func, dec, *args):
    @dec(args)
    def Decorated(param: GenBulletParam):
        func(param)
    return Decorated


def GenBullet(param: GenBulletParam):
    bullet = GameEntry.GameMain.entityManager.ShowEntity(param.type, param.pos)
    bullet.Speed = param.speed


class BulletGenerator():
    _BulletMusic: list
    _SleepTimer: int
    _Iter: Iterator

    def SetBulletMusic(self, bulletMusic: list):
        self._SleepTimer = 0
        self._BulletMusic = bulletMusic
        self._Iter = iter(self._BulletMusic)

    def PlayBulletMusic(self, param: GenBulletParam):
        if(self._SleepTimer > 0):
            self._SleepTimer -= 1
            return
        func = GenBullet
        while True:
            try:
                key = next(self._Iter)
            except:
                self._Iter = iter(self._BulletMusic)
                break
            data = key[0]
            if(data == Decs.Double):
                func = Decorator(func, DoubleBullet, key[1])
            elif(data == Decs.Triple):
                func = Decorator(func, TripleBullet, key[1])
            elif(data == Decs.Circle):
                func = Decorator(func, CircleBullet, key[1])
            elif(data == Decs.Offset):
                func = Decorator(
                    func, OffsetBullet,key[1], key[2])
            elif(data == Decs.Sleep):
                self._SleepTimer = key[1]
                break
            else:
                raise Exception("Invalid param {}".format(data))
        func(param)
