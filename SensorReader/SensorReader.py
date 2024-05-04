#!/usr/bin/env python3
# @author: Markus Kösters

import json

from SensorReader.Sensors.Sensor import Sensor


class SensorReader:

    def __init__(self, busReaderMethod: callable, sensors: list[Sensor]):
        self.__busReaderMethod: callable = busReaderMethod
        self.__sensors: list[Sensor] = sensors
        self.__instancedSensorsList: list = []
        self.__sensorTypes: dict[list[Sensor]] = {}

    def getSensorReading(self) -> json:
        rawData = self.__busReaderMethod()
        self.__storeValues(rawData)

    def __storeValues(self, rawData: json):
        rawData = self.__loadJsonData(rawData)
        rawData.get()

    def __createSensor(self, rawData: dict):
        """
        Method for creating sensor-instances and
        :param rawData:
        :return:
        """
        for sensorClass in self.__sensors:
            self.__sensorTypes[sensorClass.type] = rawData.get(sensorClass.type)
            sensorValues: list = rawData.get(sensorClass.type)  # sensors contains a list with multiple values
            for valueCounter, value in enumerate(sensorValues):
                newSensorInstance = sensorClass(valueCounter, value=value)  # This would make the sensors have an id that is only unique to the sensortype but not to all sensors
                self.__sensorTypes.setdefault(sensorClass.type).append(newSensorInstance)  # creating sensor-instances and adding those to the sensortypes

    @staticmethod
    def __loadJsonData(jsonData: json) -> dict:
        """
        Method for converting a json into a dictionary.
        :param jsonData: Json-document that is to be converted.
        :return: Dictionary containing the data of the json-document.
        """
        data: dict = json.loads(jsonData)
        return data
