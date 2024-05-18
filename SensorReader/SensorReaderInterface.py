#!/usr/bin/env python3
# @author: Markus Kösters

from abc import ABC, abstractmethod


class SensorReaderInterface(ABC):

    @abstractmethod
    def readSensorData(self) -> None:
        """
        Getter-Method for getting sensor data.
        :return: Dictionary containing sensor data.
        """

    @abstractmethod
    def subscribeToSensorData(self, callbackMethod: callable) -> None:
        """
        Method for subscribing to sensor data.
        :param callbackMethod: Method that receives sensor data in case of an update.
        :return: Dictionary containing sensor data.
        """

        