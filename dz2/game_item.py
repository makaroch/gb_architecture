from abc import ABC, abstractmethod


class IGameItem(ABC):
    @abstractmethod
    def open(self) -> None:
        pass


class Gem(IGameItem):
    def open(self) -> None:
        print("This is gem!!!")


class Gold(IGameItem):
    def open(self) -> None:
        print("This is gold")


class Item1(IGameItem):
    def open(self) -> None:
        print("This is Item1")


class Item2(IGameItem):
    def open(self) -> None:
        print("This is Item2")


class Item3(IGameItem):
    def open(self) -> None:
        print("This is Item3")


class Item4(IGameItem):
    def open(self) -> None:
        print("This is Item4")


class Item5(IGameItem):
    def open(self) -> None:
        print("This is Item5")
