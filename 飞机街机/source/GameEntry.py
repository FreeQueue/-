from Manager import *


class GameMain():
    resourceManager: ResourceManager
    inputManager: InputManager
    entityManager: EntityManager
    uiManager: UiManager
    eventManager: EventManager
    dataManager: DataManager
    levelManager: LevelManager
    managers: list

    def Init():

        GameMain.managers = []
        GameMain.resourceManager = ResourceManager()
        GameMain.inputManager = InputManager()
        GameMain.dataManager = DataManager()
        GameMain.eventManager = EventManager()
        GameMain.entityManager = EntityManager()
        GameMain.uiManager = UiManager()
        GameMain.levelManager = LevelManager()

    def Register(manager: ManagerBase):
        GameMain.managers.append(manager)

    def Update():
        for manager in GameMain.managers:
            manager.Update()
