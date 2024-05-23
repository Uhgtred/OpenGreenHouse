#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass
from typing import Optional


@dataclass
class SoilMoistureSensor:
    sensorID: int
    # Todo: Make this getter and setter thing working so each time when the value is being changed, it is also being corrected.
    __value: Optional[int]
    # The value will be set by the application and has a range of 0 to 100 (percentage).
    # value: int = 0
    # The min and max value needs to be adapted to a specific soil-moisture sensor for calibration of this sensor.
    # minValue is typically around 200 and should be recorded with the sensor exposed to pure water, as far as possible BUT!!! Without the water touching the electronic components of the sensor (sensor will be damaged probably).
    # maxValue is typically around 500 and should be recorded when the sensor is in dry air. The sensor shall not be wet for calibrating the min-value and should also not be touched or touching metal etc.
    minValue: int = 250  # sensor-value when exposed to plain water.
    maxValue: int = 550  # sensor-value when exposed to air (not touching any metal nor skin etc.)
    type: str = 'soilMoisture'

    @property
    def value(self) -> int:
        """
        Getter-method for the value!
        :return: The content of __value.
        """
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value: int = int(round(self.__mapSensorValues(self.value), 0))

    def __mapSensorValues(self, sensor_value: int) -> float:
        """
        This method maps the sensor value to an integer value of range 0 to 100 (percentage of soilMoisture).
        :param sensor_value: The actual value that has been measured by the sensor.
        :return: The mapped value.
        """
        return 100 - ((sensor_value - self.minValue) * 100.0) / (self.maxValue - self.minValue)
