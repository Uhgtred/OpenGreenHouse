#!/usr/bin/env python3
# @author: Markus Kösters
import json
import unittest
from unittest.mock import MagicMock, patch

from BusTransactions.BusFactory import BusFactory
from SensorReader import SensorReader
from SensorReader.SensorReaderBuilder import SensorReaderBuilder
from SensorReader.Sensors.SensorInterface import SensorInterface


class testSensor(SensorInterface):
    id = 0
    value: any = 0
    type = 'test'

class TestSensorReader(unittest.TestCase):
    def setUp(self):
        self.testSensor = testSensor()
        self.sensorReader = SensorReaderBuilder(stub=True).addHumidityTemperatureSensor(1).addSoilMoistureSensor(3).build()

    def test_readSensorData(self):
        self.sensorReader.setSensor(3, 'type', MagicMock())
        self.sensorReader.subscribeToSensorData()
        # Asserts go here

    def test_setSensor(self):
        self.sensorReader.setSensor(3, self.testSensor.id, testSensor)
        # you may want to assert that the sensors were added as expected

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

