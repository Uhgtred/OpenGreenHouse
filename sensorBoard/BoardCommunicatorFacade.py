#!/usr/bin/env python3
# @author: Markus Kösters
from typing import override


# This class shall be responsible for communicating with the sensor-board.
# This will be Facade-pattern, it handles all the communication with the sensor-board, by using already existing classes and methods.

class BoardCommunicatorFacade:
    """
    A Facade that handles most of the communication details between the sensor-board and the python-code.
    """

    def __init__(self):
        self.__readSensorData: type = None

    # This should make the method available to the calling method just like it was an usual class-attribute or method!
    @property
    def readSensorData(self) -> type:
        """
        GetterMethod for the sensor-Readings. When this getter is called, it reads the sensorData.
        :return: SensorData that has been retrieved by the sensorReader.
        """
        self.
        return self.__readSensorData()
    @override
    def __readSensorData(self):
        # soemthing to send to the sensor-board
        self.__readSensorData()
    @readSensorData.setter
    def readSensorData(self, readSensorDataMethod: type) -> None:
        """
        SetterMethod for setting the method that will be responsible for communicating to the sensor-board!
        :param readSensorDataMethod:
        :return:
        """
        self.__readSensorData = readSensorDataMethod
