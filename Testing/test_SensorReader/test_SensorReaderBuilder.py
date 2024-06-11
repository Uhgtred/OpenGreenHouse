#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from BusTransactions.BusFactory import BusFactory
from SensorReader.SensorReaderBuilder import SensorReaderBuilder


class MyTestCase(unittest.TestCase):

    def setUp(self):
        busInstanceStub = BusFactory.produceSerialTransceiver(stub=True)
        self.builder = SensorReaderBuilder(busInstanceStub)

    def test_addSoilMoistureSensor(self):
        sensorReader = self.builder.addSoilMoistureSensor(3).build()
        self.assertIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        self.assertNotIn('humidity', sensorReader._SensorReader__sensorListDictionary)
        self.assertNotIn('temperature', sensorReader._SensorReader__sensorListDictionary)
        sensorReader._SensorReader__sensorListDictionary.pop('soilMoisture')

    def test_addHumiditySensor(self):
        sensorReader = self.builder.addHumiditySensor(1).build()
        self.assertIn('humidity', sensorReader._SensorReader__sensorListDictionary)
        self.assertNotIn('temperature', sensorReader._SensorReader__sensorListDictionary)
        self.assertNotIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        sensorReader._SensorReader__sensorListDictionary.pop('humidity')

    def test_addTemperatureSensor(self):
        sensorReader = self.builder.addTemperatureSensor(1).build()
        self.assertNotIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        self.assertNotIn('humidity', sensorReader._SensorReader__sensorListDictionary)
        self.assertIn('temperature', sensorReader._SensorReader__sensorListDictionary)
        sensorReader._SensorReader__sensorListDictionary.pop('temperature')

    def test_addAllSensors(self):
        sensorReader = self.builder.addHumiditySensor(1).addTemperatureSensor(1).addSoilMoistureSensor(3).build()
        self.assertIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        self.assertIn('temperature', sensorReader._SensorReader__sensorListDictionary)
        self.assertIn('humidity', sensorReader._SensorReader__sensorListDictionary)
        sensorReader._SensorReader__sensorListDictionary.pop('temperature')
        sensorReader._SensorReader__sensorListDictionary.pop('humidity')
        sensorReader._SensorReader__sensorListDictionary.pop('soilMoisture')


if __name__ == '__main__':
    unittest.main()
