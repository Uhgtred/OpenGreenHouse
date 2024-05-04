#!/usr/bin/env python3
# @author: Markus Kösters
from dataclasses import dataclass

from SensorReader.Sensors.Sensor import Sensor


@dataclass
class SoilMoistureSensor(Sensor):
    id: int
    value: int = 0
    minValue: int = 0 # sensor-value when exposed to air
    maxValue: int = 100 # sensor-value when exposed to plain water
    type: str = 'SoilMoistureSensor'

    def __post_init__(self):
        self.value: int = int(round(self.__mapValue(self.value), 0))

    def __mapValue(self, value: int):
        return (value - self.minValue) * 100 / (self.maxValue - self.minValue)