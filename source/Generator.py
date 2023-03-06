import random
from typing import Tuple
import GameEntry
import Data
from Param import EnumEntity, EnumEvent


class EnemyGenerator():
    EnemyMusic: dict

    def SetMusic(self, music: dict):
        self.EnemyMusic = music
        self._LastTime = -1
        self._iter = iter(self.EnemyMusic)

    def Update(self):
        while(GameEntry.GameMain.dataManager.runData.Time > self._LastTime):
            try:
                self._LastTime = next(self._iter)
            except:
                break
            pair = self.EnemyMusic[self._LastTime]
            self.GenEnemy(pair[0], pair[1])

    def GenEnemy(self,enum: EnumEntity, pos: Tuple[int, int] = (0, 0)):
        GameEntry.GameMain.entityManager.ShowEntity(enum,pos)


class SupplyGenerator():
    def __init__(self) -> None:
        GameEntry.GameMain.eventManager.Register(
            EnumEvent.Supply, self.GenSupply)

    def GenSupply(self, event):
        GameEntry.GameMain.entityManager.ShowEntity(
            EnumEntity.BombSupply, (random.randint(20, Data.DefaultData.Width-20), 0))
