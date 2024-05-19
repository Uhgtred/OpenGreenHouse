#!/usr/bin/env python3
# @author: Markus Kösters
from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class Sensor(ABC):
    """
    Dataclass for prescribing the structure of a Sensor-object.
    """
    id: int
    __value: any
    type: str

    @property
    @abstractmethod
    def value(self) -> any:
        return self.__value

    @value.setter
    @abstractmethod
    def value(self, value: any) -> None:
        pass
