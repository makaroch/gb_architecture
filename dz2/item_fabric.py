from dz2.game_item import *


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self) -> IGameItem:
        pass



class GemGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Gem()


class GoldGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Gold()



class Item1Generator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Item1()


class Item2Generator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Item2()


class Item3Generator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Item3()


class Item4Generator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Item4()


class Item5Generator(ItemFabric):
    def create_item(self) -> IGameItem:
        return Item5()
