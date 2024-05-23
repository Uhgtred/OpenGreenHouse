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
    return json.dumps({'tempHumidity': [{'temperature': 9, 'humidity': 9}], 'soilMoisture': [9, 9, 9]})


class TestSensorReader(unittest.TestCase):
    def setUp(self):
        self.testSensor = testSensor
        self.sensorReader = SensorReader.SensorReader(busReaderStub)
        self.data = {}

    def receiveSensorData(self, data: any):
        self.data = data

    def test_readSensorData(self):
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        self.sensorReader.subscribeToSensorData(self.receiveSensorData)
        self.sensorReader.readSensorData()
        self.assertDictEqual(self.data, {'soilMoisture': [testSensor(sensorID=1, _testSensor__value=9), testSensor(sensorID=2, _testSensor__value=9), testSensor(sensorID=3, _testSensor__value=9)]})

    def test_setSensor(self):
        self.sensorReader.setSensor(3, self.testSensor.type, self.testSensor)
        sensorList = self.sensorReader._SensorReader__sensorListDictionary.get(self.testSensor.type)
        sensorIDList = [sensor.sensorID for sensor in sensorList]
        self.assertListEqual(sensorIDList, [1, 2, 3])

    def test_subscribeToSensorData(self):
        callback = MagicMock()
        self.sensorReader.subscribeToSensorData(callback)
        # here you may want to assert that the callback was added to __subscribers

    # Mock busReaderMethod so it returns a json
    @patch.object(SensorReader, "_SensorReader__busReaderMethod", return_value=json.dumps({"type": "value"}))
    def test_readSensorData_no_sensors(self, bus_method_mock):
        with self.assertRaises(AttributeError):
            self.sensorReader.readSensorData()

    # other tests go here...


if __name__ == '__main__':
    unittest.main()
