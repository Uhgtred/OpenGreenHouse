#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass
from typing import Optional


@dataclass
class TemperatureSensor:
    """
    Data-class for storing information about one Temperature-Humidity Sensor.
    """
    sensorID: int
    # Initialize the 'offSet' variable with an integer type. This variable is used to calibrate the sensor-values.
    # By default, it is set to 0.
    __value: Optional[float] = None
    offSet: float = 0
    type: str = 'temperature'

    @property
    def value(self) -> float:
        """
        Getter-method for the sensor-values.
        :return: Sensor-values in a dictionary with the keys: "temperature" and "humidity" and float as the according values.
        """
        return self.__value

    @value.setter
    def value(self, value: float) -> None:
        """
        Setter-method for the value of the sensor. Also, it is applying the offSet (+) to the raw value!
        :param value: value that has been read by the sensor.
        """
        self.__value = value + self.offSet
