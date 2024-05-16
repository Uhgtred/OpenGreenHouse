#!/usr/bin/env python3
# @author: Markus Kösters

import json

from SensorReader.SensorReaderConfig import SensorReaderConfig
from SensorReader.Sensors.SensorInterface import Sensor


class SensorReader:

    def __init__(self, config: SensorReaderConfig):
        self.__busReaderMethod: callable = config.busReaderMethod
        self.__sensorLists: list[list[Sensor]] = config.listOfSensorLists

    def getSensorReading(self) -> json:
        rawData: json = self.__busReaderMethod()
        dictData: dict = self.__loadJsonDataAsDict(rawData)
        self.__iterateSensorLists(self.__sensorLists, dictData)
        # Todo: add Values which are being stored to the self.__sensorLists by __iterateSensorLists to a database!

    @staticmethod
    def __iterateSensorListsAndStoreValues(sensorLists: list[list[Sensor]], dictData: dict) -> None:
        """
        Method that reads any sensor in the list of lists and adds the according value in the data-dictionary to it's value!
        :param sensorLists: List of lists of sensors.
        :param dictData: Dictionary containing the sensor data.
        """
        for sensorList in sensorLists:
            for sensorIdCounter, sensorObject in enumerate(sensorList):
                sensorObject.value = dictData.get(sensorObject.type)[sensorIdCounter]

    @staticmethod
    def __loadJsonDataAsDict(jsonData: json) -> dict:
        """
        Method for converting a json into a dictionary.
        :param jsonData: Json-document that is to be converted.
        :return: Dictionary containing the data of the json-document.
        """
        data: dict = json.loads(jsonData)
        return data
