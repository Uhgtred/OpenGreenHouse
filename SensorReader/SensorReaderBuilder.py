#!/usr/bin/env python3
# @author: Markus Kösters

from BusTransactions.BusFactory import BusFactory
from SensorReader import SensorReader
from SensorReader.Sensors.HumiditySensor import HumiditySensor
from SensorReader.Sensors.SoilMoistureSensor import SoilMoistureSensor


class SensorReaderBuilder:
    """
    Class for creating a SensorReader-instance with all wished configurations.
    """

    def __init__(self):
        self.sensorReader = SensorReader.SensorReader(BusFactory.produceSerialTransceiver())

    # @classmethod
    # def createSensorReader(cls, sensorReaderConfig: SensorReaderConfig):
    #     """
    #     Factory-method for creating a sensor-reader-instance.
    #     :param busReaderMethod: Bus that the sensor-board is communicating on.
    #     :return: SensorReader instance.
    #     """
    #     sensorReaderConfig.listOfSensorLists: list[list[Sensor]]
    #     sensorReaderConfig.listOfSensorLists.append(cls.__createSensorObject(HumiditySensor, 1))
    #     return SensorReader.SensorReader(sensorReaderConfig)

    def addHumidityTemperatureSensor(self, amount: int) -> SensorReaderBuilder:
        """
        Method for adding a Humidity-temperature-sensor to the SensorReader-instance.
        :param amount: Number of humidity-temperature-sensors that will be added.
        :return: Instance of the SensorReaderBuilder.
        """
        sensor = HumiditySensor
        self.sensorReader.setSensor(amount, sensor.type, sensor)
        return self

    def addSoilMoistureSensor(self, amount: int) -> SensorReaderBuilder:
        """
        Method for creating multiple sensor instances.
        :param amount: Number of soilmoisture-sensors that will be added.
        :return: Instance of the SensorReaderBuilder.
        """
        sensor = SoilMoistureSensor
        self.sensorReader.setSensor(amount, sensor.type, sensor)
        return self

    def build(self) -> SensorReader.SensorReader:
        """
        Method for building the instance of the SensorReader.
        :return: SensorReader Object.
        """
        return self.sensorReader
