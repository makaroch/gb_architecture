from ModelElemenst import *
from abc import ABC
from typing import List

class IModelChangedObserver(ABC):
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    def notify_change(self, sender: IModelChanger):
        pass


class ModelStore(IModelChanger):
    def __int__(self, changed_observer: List[IModelChangedObserver]) -> None:
        self.models: List[PoligonalModel] = [PoligonalModel()]
        self.scenes: List[Scene] = [Scene()]
        self.flashes: List[Flash] = [Flash()]
        self.cameras: List[Camera] = [Camera()]
        self._change_observers: IModelChangedObserver

    def get_scena(self, id: int) -> Scene:
        for scene in self.scenes:
            if scene.id == id:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass