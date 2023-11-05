from enum import Enum
from typing import List


class Texture:
    pass


class Point3D:
    pass


class Angle3D:
    pass


class Color(Enum):
    pass


class Poligon:
    def __int__(self):
        self.points = Point3D()


class PoligonalModel:
    def __int__(self, texture: List[Texture]):
        self.texture = texture
        self.poligons: List[Poligon] = [Poligon()]


class Camera:
    def __int__(self):
        self.location: Point3D
        self.angle: Angle3D

    def rotate(self, angle: Angle3D) -> None:
        pass

    def move(self, point: Point3D) -> None:
        pass


class Flash:
    def __int__(self):
        self.location: Point3D
        self.angle: Angle3D
        self.color: Color
        self.power: float

    def rotate(self, angle: Angle3D) -> None:
        pass

    def move(self, point: Point3D) -> None:
        pass


class Scene:
    __id = 0

    def __int__(self, models: List[PoligonalModel], flashes: list[Flash], cameras: List[Camera]):
        self.id: int = Scene.__id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras
        Scene.__id += 1

    def metod1(self, x: Type) -> Type:
        pass

    def metod2(self, x: Type, y: Type) -> Type:
        pass
