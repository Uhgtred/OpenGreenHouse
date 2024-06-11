#!/usr/bin/env python3
# @author: Markus Kösters

import json
import unittest
from dataclasses import dataclass
from typing import Optional
from unittest.mock import MagicMock, patch

from SensorReader import SensorReader


@dataclass
class testSensor:
    sensorID: int
    type = 'soilMoisture'
    __value: Optional[any] = 0

    @property
    def value(self) -> any:
        return self.__value

    @value.setter
    def value(self, value: any) -> None:
        self.__value = value


def busReaderStub():
    # structure that will be returned by the sensor-reader.
    return json.dumps({'temperature': [9], 'soilMoisture': [9, 9, 9], 'humidity': [9]})


def busWriterStub():
    pass


def busReaderStubWrongType():
    return {'tempHumidity': [{'temperature': 9, 'humidity': 9}], 'soilMoisture': [9, 9, 9]}


class TestSensorReader(unittest.TestCase):
    def setUp(self):
        self.testSensor = testSensor
        self.sensorReader = SensorReader.SensorReader(busReaderStub, busWriterStub)
        self.data = {}
        self.assertionDict = {'soilMoisture': [testSensor(sensorID=1, _testSensor__value=9), testSensor(sensorID=2, _testSensor__value=9), testSensor(sensorID=3, _testSensor__value=9)]}

    def receiveSensorData(self, data: any):
        self.data = data

    def test_readSensorData(self):
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        self.sensorReader.readSensorData()
        self.assertDictEqual(self.assertionDict, self.sensorReader._SensorReader__sensorListDictionary)

    def test_readSensorDataWrongType(self):
        sensorReader = SensorReader.SensorReader(busReaderStubWrongType, busWriterStub)
        self.assertRaises(TypeError, sensorReader.readSensorData)

    def test_subscribeToSensorData(self):
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        self.sensorReader.subscribeToSensorData(self.receiveSensorData)
        self.sensorReader.readSensorData()
        self.assertDictEqual(self.data, self.assertionDict)

    def test_subscribeToSensorDataWrongSensorType(self):
        self.testSensor.type = 'testSensorWrongType'
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        self.sensorReader.subscribeToSensorData(self.receiveSensorData)
        self.assertRaises(TypeError, self.sensorReader.readSensorData)

    def test_setSensor(self):
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        sensorList = self.sensorReader._SensorReader__sensorListDictionary.get(self.testSensor.type)
        sensorIDList = [sensor.sensorID for sensor in sensorList]
        self.assertListEqual(sensorIDList, [1, 2, 3])

    def test_readSensorData_no_sensors(self):
        self.assertRaises(AttributeError, self.sensorReader.readSensorData)


if __name__ == '__main__':
    unittest.main()
