#!/usr/bin/env python3
# @author: Markus Kösters

import json

from SensorReader.SensorReaderInterface import SensorReaderInterface
from SensorReader.Sensors.SensorInterface import SensorInterface


class SensorReader(SensorReaderInterface):
    """
    Class for Reading raw sensor-values from a bus.
    """

    def __init__(self, busReaderMethod: callable):
        self.__busReaderMethod: callable = busReaderMethod
        self.__sensorListDictionary: dict[str, list[object]] = {}
        self.__subscribers: set[callable] = set()

    def readSensorData(self) -> None:
        """
        Method for reading sensor-values from a bus.
        """
        rawData: json = self.__busReaderMethod()
        dictData: dict = self.__loadJsonDataAsDict(rawData)
        if len(self.__sensorListDictionary) > 0:
            self.__iterateSensorListsAndStoreValues(self.__sensorListDictionary, dictData)
            self.__notifySubscribers(self.__subscribers, self.__sensorListDictionary)
        else:
            raise AttributeError('[SensorReader]: No Sensors have been initialized. Cannot read sensors!')

    @staticmethod
    def __notifySubscribers(subscribers: set[callable], data: dict) -> None:
        """
        Method for notifying subscribers about sensor-values.
        :param subscribers: Subscribers to notify.
        :param data: Data that will be provided to subscribers.
        """
        for subscriber in subscribers:
            subscriber(data)

    @staticmethod
    def __iterateSensorListsAndStoreValues(sensorListDictionary: dict[str, list[callable]], dictData: dict) -> None:
        """
        Method that reads any sensor in the list of lists and adds the according value in the data-dictionary to it's value!
        :param sensorLists: Dictionary containing lists of sensors.
        :param dictData: Dictionary containing the sensor data.
        """
        for sensorListKey, sensorList in sensorListDictionary.items():
            for sensorIdCounter, sensorObject in enumerate(sensorList):
                try:
                    sensorObject.value = dictData.get(sensorObject.type)[sensorIdCounter]
                except TypeError:
                    raise TypeError(f'[SensorReader]: Sensordata has no value with type {sensorObject.type}!')
                
    @staticmethod
    def __loadJsonDataAsDict(jsonData: json) -> dict:
        """
        Method for converting a json into a dictionary.
        :param jsonData: Json-document that is to be converted.
        :return: Dictionary containing the data of the json-document.
        """
        try:
            data: dict = json.loads(jsonData)
            return data
        except TypeError as error:
            raise TypeError('[SensorReader]: Could not load json-data as dictionary.', error)

    def setSensor(self, amount: int, sensorType: str, sensorClass: callable) -> None:
        """
        Setter-method for the humiditySensors
        :param amount: Number of sensor that will be added to the sensorListDictionary.
        :param sensorType: Type of which the created sensorObject is.
        :param sensorClass: Dataclass that describes the structure of the sensor.
        """
        self.__sensorListDictionary.setdefault(sensorType, [])
        currentListLength = len(self.__sensorListDictionary.get(sensorType))
        for idCounter in range(amount):
            # setting the current id to the last element of the list + the idCounter
            id_ = idCounter + 1 + currentListLength
            self.__addSensorOfType(sensorType, id_, sensorClass)

    def __addSensorOfType(self, sensorType: str, sensorID: int, sensorClass: type(SensorInterface)) -> None:
        """
        Method for adding a sensor of any type to the sensorListDictionary.
        :param sensorType: Type of the sensor, so it can be added to the dictionary at a specific value
        :param sensorID: ID that is going to be stored for the sensor-instance created.
        :param sensorClass: Dataclass that describes the structure of the sensor.
        """
        sensorObject: object = sensorClass(sensorID)
        self.__sensorListDictionary.setdefault(sensorType, []).append(sensorObject)

    def subscribeToSensorData(self, callbackMethod: callable) -> None:
        """
        Method for adding a subscriber to the SensorReader. Each subscriber can only be added once.
        :param callbackMethod: Method that will be called if an update of sensorData is received.
        """
        self.__subscribers.add(callbackMethod)
