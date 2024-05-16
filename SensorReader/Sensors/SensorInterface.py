#!/usr/bin/env python3
# @author: Markus Kösters
from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class Sensor(ABC):
    """
    Dataclass for prescribing the structure of a Sensor-object.
    """
    type: str
    id: int
    __value: any

    @abstractmethod
    @property
    def value(self) -> any:
        return self.__value

    @abstractmethod
    @value.setter
    def value(self, value: any) -> None:
        pass
