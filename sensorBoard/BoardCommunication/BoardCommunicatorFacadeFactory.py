#!/usr/bin/env python3
# @author: Markus Kösters
from SensorReader.SensorReaderBuilder import SensorReaderBuilder
from sensorBoard.BoardCommunication.BoardCommunicatorFacade import BoardCommunicatorFacade


class BoardCommunicatorFacadeFactory:

    @staticmethod
    def produceBoardCommunicatorFacade(stub: bool = False, sensorReaderMethod: callable = 'default') -> BoardCommunicatorFacade:
        """
        Method for creating a facade.
        :return: A facade-object that handles most of the communication details between the sensor-board and the python-code.
        """
        facade = BoardCommunicatorFacade(stub=stub)
        sensorReader = SensorReaderBuilder(sensorReaderMethod).addHumidityTemperatureSensor(1).addSoilMoistureSensor(3).build()
        facade.readSensorData = sensorReader
        return facade
