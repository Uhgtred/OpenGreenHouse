#!/usr/bin/env python3
# @author: Markus Kösters

from dataclasses import dataclass

import BusTransactions
from SensorReader.Sensors.SensorInterface import Sensor


@dataclass
class SensorReaderConfig:
    """
    Dataclass setting the configuration of the sensor reader.
    """
    listOfSensorLists: list[list[Sensor]]
    busReaderMethod: callable = BusTransactions.BusFactory.BusFactory.produceSerialTransceiver()
