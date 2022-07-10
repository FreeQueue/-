from math import sin
import random
import pygame
import GameEntry
from BulletGeneraTool import BulletGenerator, GenBulletParam
from DataBase import BulletData, EnemyData, EntityDataBase
import Data
from Param import EnumGroup, EnumEntity, EnumEvent,EnumSound


class EntityBase(pygame.sprite.Sprite):
    Speed: pygame.Vector2
    _Active = False
    Type: EnumEntity
    CollideGroup = EnumGroup.Other

    def __init__(self, data: EntityDataBase):
        pygame.sprite.Sprite.__init__(self)
        self.Speed = data.Speed
        self.image = GameEntry.GameMain.resourceManager.GetImage(
            data.Image)
        self.rect = self.image.get_rect()

    @property
    def Active(self) -> bool:
        return self._Active

    @Active.setter
    def Active(self, value: bool):
        self._Active = value

    def Hide(self):
        GameEntry.GameMain.entityManager.HideEntity(self)

    def OnShow(self):
        self.Active = True

    def update(self):
        if(self.Active):
            self.Move()
            self.Fire()
            self.CollideCheck()

    def OnHide(self):
        self.Active = False

    def BuildBulletGenerator(self, bulletMusic: list, param: GenBulletParam):
        self._BulletGenerator = BulletGenerator()
        self._BulletGenerator.SetBulletMusic(bulletMusic)
        self._GenBulletParam = param

    def CollideCheck(self):
        pass

    def Move(self):       
        if(not self.rect.colliderect(GameEntry.GameMain.uiManager.ScreenRect)):
            self.Hide()
        self.rect.centerx += self.Speed.x
        self.rect.centery += self.Speed.y

    def Fire(self):
        if(hasattr(self, "_BulletGenerator")):
            self._GenBulletParam.pos=self.rect.center
            self._BulletGenerator.PlayBulletMusic(self._GenBulletParam)

    def Hit(self, damage: int = 1):
        self.Hide()


class SupplyEntity(EntityBase):
    CollideGroup=EnumGroup.Supply
    def CollideCheck(self):
        hitEntity = pygame.sprite.spritecollide(
            self, GameEntry.GameMain.entityManager.GetGroup(EnumGroup.Player), False, pygame.sprite.collide_mask)
        if(hitEntity):
            GameEntry.GameMain.dataManager.runData.Bomb += 1
            GameEntry.GameMain.resourceManager.GetSound(Data.DefaultData.SoundDic[EnumSound.GetBomb]).play()
            self.Hide()


class BulletEntity(EntityBase):
    _HitGroup: pygame.sprite.Group
    Damage: int

    def __init__(self, data: BulletData):
        super().__init__(data)
        self._HitGroup = GameEntry.GameMain.entityManager.GetGroup(
            data.HitGroup)
        self.Damage = data.Damage
    # def Move(self):
    #     super().Move()
    def CollideCheck(self):
        hitEntity = pygame.sprite.spritecollide(
            self, self._HitGroup, False, pygame.sprite.collide_mask)
        if(hitEntity):
            self.Active = False
            for entity in hitEntity:
                entity.Hit()
            self.Hide()


class EnemyEntity(EntityBase):
    _Data: EnemyData
    _DieTimer: int
    _Health: int
    CollideGroup = EnumGroup.Enemies
    SpanTime=10
    SpanTimer=0
    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, value):
        self._Health = value
        if(self._Health <= 0):
            self.Dead()

    def __init__(self, data: EnemyData):
        super().__init__(data)
        self._Data = data
        self.BuildBulletGenerator(data.BulletMusic, data.BulletParam)

    def OnShow(self):
        super().OnShow()
        self.image=GameEntry.GameMain.resourceManager.GetImage(
                self._Data.Image)
        self._Health = self._Data.OriginHealth
        self._DieTimer = 0

    def update(self):
        super().update()
        self.Dying()

    def Hit(self, damage: int = 1):
        self.Health -= damage

    def CollideCheck(self):
        hitEntity = pygame.sprite.spritecollide(
            self, GameEntry.GameMain.entityManager.GetGroup(EnumGroup.Player), False, pygame.sprite.collide_mask)
        if(hitEntity):
            hitEntity[0].Hit(self.Health)
            self.Hide()

    def Dead(self):
        self.Active = False
        GameEntry.GameMain.dataManager.runData.Score += self._Data.Score
        GameEntry.GameMain.resourceManager.GetSound(
            self._Data.DestroySound).play()

    def Dying(self):
        self.SpanTimer-=1
        if(self.SpanTimer>0):return
        self.SpanTimer=self.SpanTime
        if(not self.Active):
            self.image = GameEntry.GameMain.resourceManager.GetImage(
                self._Data.DestroyImages[self._DieTimer])
            self._DieTimer += 1
            if(self._DieTimer == len(self._Data.DestroyImages)):
                self.Hide()


class Boss(EnemyEntity):
    def OnShow(self):
        super().OnShow()
        self.rect.topleft = (Data.DefaultData.Width/2, 0)

    def update(self):
        super().update()
        self.Enter()

    def Move(self):
        pass
    def OnHide(self):
        super().OnHide()
        GameEntry.GameMain.eventManager.Fire(EnumEvent.GameFinish)
    def Enter(self):
        if(self.Active == True):
            return
        self.rect.centery += 1
        if(self.rect.centery == self.rect.height):
            self.enterFlag = True
            self.Active = True


class PlayerEntity(EnemyEntity):
    Speed: int
    CollideGroup = EnumGroup.Player
    HitTimer: int
    HitTime = 60
    BombTimer = 0
    BombTime = 120

    def __init__(self, data: EnemyData):
        super().__init__(data)
        self.Speed = Data.DefaultData.DefaultPlayerSpeed

    def OnShow(self):
        super().OnShow()
        self.HitTimer = 120

    def update(self):
        super().update()
        self.HitTimer -= 1
        if(self.HitTimer > 0):
            self.image.set_alpha(255*abs(sin(self.HitTimer/6)))
        else:
            self.image.set_alpha(255)
        self.BombTimer -= 1

    def OnHide(self):
        super().OnHide()
        GameEntry.GameMain.eventManager.Fire(EnumEvent.GameOver)

    def CollideCheck(self):
        pass

    def Hit(self, damage: int = 1):
        if(self.HitTimer > 0):
            return
        super().Hit(damage)
        self.HitTimer = self.HitTime

    def Move(self):
        if(self.Active):
            if(GameEntry.GameMain.inputManager.Up):
                self.moveUp()
            if(GameEntry.GameMain.inputManager.Down):
                self.moveDown()
            if(GameEntry.GameMain.inputManager.Left):
                self.moveLeft()
            if(GameEntry.GameMain.inputManager.Right):
                self.moveRight()
            if(GameEntry.GameMain.inputManager.Space):
                self.Bomb()

    def Bomb(self):
        if(self.BombTimer > 0):
            return
        self.BombTimer = self.BombTime
        GameEntry.GameMain.dataManager.runData.Bomb -= 1
        GameEntry.GameMain.resourceManager.GetSound(
            Data.DefaultData.SoundDic[EnumSound.UseBomb]).play()
        for enemy in GameEntry.GameMain.entityManager.GetGroup(EnumGroup.Enemies).sprites():
            enemy.Hit(10)
        GameEntry.GameMain.entityManager.ClearGroup(EnumGroup.Other)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.Speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < Data.DefaultData.Height - 60:
            self.rect.top += self.Speed
        else:
            self.rect.bottom = Data.DefaultData.Height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.Speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < Data.DefaultData.Width:
            self.rect.left += self.Speed
        else:
            self.rect.right = Data.DefaultData.Width
