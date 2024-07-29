#!/usr/bin/env python3
# @author: Markus Kösters
from API import API_Setup
from Database.DatabaseController import DatabaseController
from Database.DatabaseManipulator import DatabaseManipulator
from Database.SQLiteDatabases.SQLiteSensordataDatabase import SQLiteSensordataDatabase
from Runners import ThreadRunner
from BusTransactions.BusFactory import BusFactory
from SensorReader.SensorReaderBuilder import SensorReaderBuilder


class Main:

    def __init__(self):
        self.sensorReader = None
        self.API_port: int = 2001
        self.databaseController: DatabaseController = DatabaseController()
        self.sensorDataDatabaseManipulator = DatabaseManipulator(SQLiteSensordataDatabase)

    def main(self):
        """
        Main Method handling the workflow of the program.
        :return:
        """
        self.createSensorReader()
        self.subscribeToSensorData()

    def createDatabaseConnections(self):
        """
        Method for creating the needed databases.
        TODO: Create the dataclasses for the mentioned databases.
        """
        self.databaseController.openDatabase(SensorSettingsDatabase)
        self.databaseController.openDatabase(SQLiteSensordataDatabase)

    def createSensorReader(self) -> None:
        """
        Method that creates the sensor reader instance.
        """
        busInstance = BusFactory.produceSerialTransceiver()
        self.sensorReader = SensorReaderBuilder(busInstance).addSoilMoistureSensor(3).addHumiditySensor(1).addTemperatureSensor(1).build()

    def subscribeToSensorData(self) -> None:
        """
        Method handling the subscriptions of the sensor reader data.
        """
        self.sensorReader.subscribeToSensorData(self.sensorDataDatabaseManipulator.insertData)

    def setupAPI(self) -> None:
        """
        Method that creates the API instance.
        """
        API_Setup(self.API_port).run()
