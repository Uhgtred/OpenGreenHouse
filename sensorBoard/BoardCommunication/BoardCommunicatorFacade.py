#!/usr/bin/env python3
# @author: Markus Kösters
from typing import override

from BusTransactions.BusFactory import BusFactory
from SensorReader.SensorReaderBuilder import SensorReaderBuilder


# This class shall be responsible for communicating with the sensor-board.
# This will be Facade-pattern, it handles all the communication with the sensor-board, by using already existing classes and methods.

class BoardCommunicatorFacade:
    """
    A Facade that handles most of the communication details between the sensor-board and the python-code.
    """

    def __init__(self):
        self.__busReader = BusFactory.produceSerialTransceiver()
        self.sensorReader = SensorReaderBuilder(self.__busReader).addHumidityTemperatureSensor(1).addSoilMoistureSensor(3).build()
        # setting the method that will read from the bus. This also sets the getter-method
        self.readSensorData = self.__busReader.readSingleMessage()

    # This should make the method available to the calling method just like it was a usual class-attribute or method!
    @property
    def readSensorData(self) -> type:
        """
        GetterMethod for the sensor-Readings. When this getter is called, it reads the sensorData.
        :return: SensorData that has been retrieved by the sensorReader.
        """
        # Todo: define some message that will be set on the microcontroller as well as this side.
        # temporary hardcoded message that will tell the sensor-board to return the sensordata.
        try:
            self.__busReader.writeSingleMessage(b'1')
            return self.__readSensorData()
        except Exception as exception:
            raise AttributeError(f'Retrieving Sensor-data failed: {exception}')

    @readSensorData.setter
    def readSensorData(self, readSensorDataMethod: type) -> None:
        """
        SetterMethod for setting the method that will be responsible for communicating to the sensor-board!
        :param readSensorDataMethod:
        :return:
        """
        self.__readSensorData = readSensorDataMethod
