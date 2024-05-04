#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from SensorReader.Sensors.Sensor import Sensor


@dataclass
class HumiditySensor(Sensor):
    id: int
    value: dict[str, float] = 0
    # Initialize the 'offSet' variable with integer type. This variable is used to indicate
    # the displacement or difference from a reference position in the data structure or resource.
    # Initially, it is set to 0.
    offSet: int = 0
    type: str = 'HumidityTemperatureSensor'
