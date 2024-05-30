#!/usr/bin/env python3
# @author: Markus Kösters

import typing

from BusTransactions.BusInterface import BusInterface
from SensorReader import SensorReader
from SensorReader.Sensors.HumiditySensor import HumiditySensor
from SensorReader.Sensors.SoilMoistureSensor import SoilMoistureSensor


class SensorReaderBuilder:
    """
    Class for creating a SensorReader-instance with all wished configurations.
    """

    def __init__(self, busInstance: type(BusInterface)) -> None:
        """
        Init-Method for the SensorReaderBuilder class.
        :param busInstance: Instance of the Bus class.
        """
        sensorReaderMethod = busInstance.readSingleMessage
        sensorWriterMethod = busInstance.writeSingleMessage
        self.sensorReader = SensorReader.SensorReader(sensorReaderMethod, sensorWriterMethod)

    def addHumidityTemperatureSensor(self, amount: int) -> typing.Self:
        """
        Method for adding a Humidity-temperature-sensor to the SensorReader-instance.
        :param amount: Number of humidity-temperature-sensors that will be added.
        :return: Instance of the SensorReaderBuilder.
        """
        sensor = HumiditySensor
        self.sensorReader.setSensor(amount, sensor.type, sensor)
        return self

    def addSoilMoistureSensor(self, amount: int) -> typing.Self:
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
