#!/usr/bin/env python3
# @author: Markus Kösters

import BusTransactions
from SensorReader import SensorReader
from SensorReader.SensorReaderConfig import SensorReaderConfig
from SensorReader.Sensors.HumiditySensor import HumiditySensor
from SensorReader.Sensors.SensorInterface import Sensor
from SensorReader.Sensors.SoilMoistureSensor import SoilMoistureSensor


class SensorReaderFactory:

    @staticmethod
    def createSensorReader(sensorReaderConfig: SensorReaderConfig):
        """
        Factory-method for creating a sensor-reader-instance.
        :param busReaderMethod: Bus that the sensor-board is communicating on.
        :return: SensorReader instance.
        """
        return SensorReader.SensorReader(sensorReaderConfig)

    def __createSensorObject(self, sensorClass: Sensor, numberOfSensors: int) -> list[Sensor]:
        """
        Method for creating multiple sensor instances.
        :param sensorClass: Dataclass that is used to create the sensor instances.
        :param numberOfSensors: Amount of sensor instances that will be created.
        :return: List containing multiple sensor instances.
        """
        # Todo: There needs to be a database containing information about the sensor, so calibrations don't have to be done each time.
        sensorInstanceList: list[Sensor] = []
        for counter in range(numberOfSensors):
            # fill data from Database as the argument of this method!
            sensorClass('nothingYet')
        return sensorInstanceList