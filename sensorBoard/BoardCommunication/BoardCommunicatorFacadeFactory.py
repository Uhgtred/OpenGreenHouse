#!/usr/bin/env python3
# @author: Markus Kösters
from SensorReader.SensorReaderBuilder import SensorReaderBuilder
from sensorBoard.BoardCommunication.BoardCommunicatorFacade import BoardCommunicatorFacade


class BoardCommunicatorFacadeFactory:

    @staticmethod
    def produceBoardCommunicatorFacade() -> BoardCommunicatorFacade:
        """
        Method for creating a facade.
        :return: A facade-object that handles most of the communication details between the sensor-board and the python-code.
        """
        facade = BoardCommunicatorFacade()
        sensorReaderMethod = SensorReaderBuilder().addHumidityTemperatureSensor(1).addSoilMoisturSensor(3).build()
        facade.readSensorData = sensorReaderMethod
        return facade
