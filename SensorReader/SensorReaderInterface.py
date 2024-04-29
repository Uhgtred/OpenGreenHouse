#!/usr/bin/env python3
# @author: Markus Kösters
from abc import ABC, abstractmethod


class SensorReaderInterface(ABC):

    @abstractmethod
    def getSensorData(self) -> dict:
        """
        Getter-Method for getting sensor data.
        :return: Dictionary containing sensor data.
        """

        