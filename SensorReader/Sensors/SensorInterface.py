#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass
from typing import Protocol, Optional


@dataclass
class SensorInterface(Protocol):
    """
    Dataclass for prescribing the structure of a Sensor-object.
    """
    sensorID: int
    __value: Optional[any]
    type: str = 'interface'

    @property
    def value(self) -> any:
        return self.__value

    @value.setter
    def value(self, value: any) -> None:
        pass
