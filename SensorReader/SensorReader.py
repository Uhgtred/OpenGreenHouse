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
        rawData: json = self.__busReaderMethod()
        dictData: dict = self.__loadJsonDataAsDict(rawData)

    @staticmethod
    def __loadJsonDataAsDict(jsonData: json) -> dict:
        """
        Method for converting a json into a dictionary.
        :param jsonData: Json-document that is to be converted.
        :return: Dictionary containing the data of the json-document.
        """
        data: dict = json.loads(jsonData)
        return data
