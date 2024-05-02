#!/usr/bin/env python3
# @author: Markus Kösters
import BusTransactions
from SensorReader import SensorReader


class SensorReaderFactory:

    @staticmethod
    def createSensorReader(busReaderMethod: BusTransactions.Bus.readSingleMessage = None):
        """
        Factory-method for creating a sensor-reader-instance.
        :param busReaderMethod: Bus that the sensor-board is communicating on.
        :return: SensorReader instance.
        """
        if not busReaderMethod:
            busReaderMethod = BusTransactions.BusFactory.BusFactory.produceSerialTransceiver()
        return SensorReader.SensorReader(busReaderMethod)
