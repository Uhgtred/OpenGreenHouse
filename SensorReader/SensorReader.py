#!/usr/bin/env python3
# @author: Markus Kösters

import json


class SensorReader:

    def __init__(self, busReaderMethod: callable):
        self.__busReaderMethod = busReaderMethod

    def getSensorReading(self) -> json:
        rawMessage = self.__busReaderMethod()

