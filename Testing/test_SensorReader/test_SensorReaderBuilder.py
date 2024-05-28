#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from SensorReader.SensorReaderBuilder import SensorReaderBuilder


def stubMethod(someArg):
    pass


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = SensorReaderBuilder(stubMethod)

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
