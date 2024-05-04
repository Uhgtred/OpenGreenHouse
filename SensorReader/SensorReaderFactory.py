#!/usr/bin/env python3
# @author: Markus Kösters
import BusTransactions
from SensorReader import SensorReader
from SensorReader.Sensors.HumiditySensor import HumiditySensor
from SensorReader.Sensors.SoilMoistureSensor import SoilMoistureSensor


class SensorReaderFactory:

    @staticmethod
    def createSensorReader(busReaderMethod: BusTransactions.Bus.readSingleMessage = None):
        """
        Factory-method for creating a sensor-reader-instance.
        :param busReaderMethod: Bus that the sensor-board is communicating on.
        :return: SensorReader instance.
        """
        sensorList: list = [HumiditySensor, SoilMoistureSensor]
        if not busReaderMethod:
            busReaderMethod = BusTransactions.BusFactory.BusFactory.produceSerialTransceiver()
        return SensorReader.SensorReader(busReaderMethod, sensorList)
