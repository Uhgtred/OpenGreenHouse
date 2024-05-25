#!/usr/bin/env python3
# @author: Markus Kösters
from SensorReader import Sensors
from SensorReader.SensorReaderBuilder import SensorReaderBuilder
from SensorReader.Sensors.HumiditySensor import HumiditySensor
from sensorBoard.BoardCommunicatorFacade import BoardCommunicatorFacade


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
