#!/usr/bin/env python3
# @author: Markus Kösters

from Runners import ThreadRunner
from BusTransactions.BusFactory import BusFactory


class Main:

    def __init__(self):
        self.__threadRunner: ThreadRunner = ThreadRunner()

    def someMethod(self):
        pass

    def main(self):
        # reading raw data from the sensorboard
        # has to go to a thread later
        bus = BusFactory.produceSerialTransceiver()
        self.__threadRunner.addTask(bus.readBusUntilStopFlag, self.someMethod)