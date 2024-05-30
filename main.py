#!/usr/bin/env python3
# @author: Markus Kösters

from Runners import ThreadRunner
from BusTransactions.BusFactory import BusFactory
from SensorReader.SensorReaderBuilder import SensorReaderBuilder


class Main:

    def __init__(self):
        self.sensorReader = None

    def main(self):
        """
        Main Method handling the workflow of the program.
        :return:
        """
        self.createSensorReader()
        self.subscribeToSensorData()

    def createSensorReader(self) -> None:
        """
        Method that creates the sensor reader instance.
        """
        busInstance = BusFactory.produceSerialTransceiver()
        self.sensorReader = SensorReaderBuilder(busInstance).addSoilMoistureSensor(3).addHumidityTemperatureSensor(1).build()

    def subscribeToSensorData(self) -> None:
        """
        Method handling the subscriptions of the sensor reader data.
        """
        self.sensorReader.subscribeToSensorData(dataBase)  # database not yet implemented!