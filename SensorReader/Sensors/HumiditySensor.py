#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

from SensorReader.Sensors.SensorInterface import Sensor


@dataclass
class HumiditySensor(Sensor):
    """
    Data-class for storing information about one Temperature-Humidity Sensor.
    """
    id: int
    # Initialize the 'offSet' variable with integer type. This variable is used to calibrate the sensor-values.
    # By default, it is set to 0.
    __value: dict[str, float] = 0
    offSetTemp: float = 0
    offSetHumidity: float = 0
    type: str = 'tempHumidity'

    @property
    def value(self) -> dict:
        """
        Getter-method for the sensor-values.
        :return: Sensor-values in a dictionary with the keys: "temperature" and "humidity" and float as the according values.
        """
        return self.__value

    @value.setter
    def value(self, value: dict) -> None:
        """
        Setter-method for the value of the sensor. Also, it is applying the offSet (+) to the raw value!
        :param value: value that has been read by the sensor.
        """
        self.__value['temperature'] = value.get('temperature') + self.offSetTemp
        self.__value['humidity'] = value.get('humidity') + self.offSetHumidity
