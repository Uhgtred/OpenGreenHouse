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
        self.assertNotIn('tempHumidity', sensorReader._SensorReader__sensorListDictionary)

    def test_add_soil_moisture_sensor(self):
        sensorReader = self.builder.addHumidityTemperatureSensor(1).build()
        self.assertNotIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        self.assertIn('tempHumidity', sensorReader._SensorReader__sensorListDictionary)

    def test_addBothSensors(self):
        sensorReader = self.builder.addHumidityTemperatureSensor(1).addSoilMoistureSensor(3).build()
        self.assertIn('soilMoisture', sensorReader._SensorReader__sensorListDictionary)
        self.assertIn('tempHumidity', sensorReader._SensorReader__sensorListDictionary)


if __name__ == '__main__':
    unittest.main()
