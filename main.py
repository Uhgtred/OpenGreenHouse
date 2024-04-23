#!/usr/bin/env python3
# @author: Markus Kösters

from BusTransactions.BusFactory import BusFactory


class Main:

    def __init__(self):
        pass

    def someMethod(self):
        pass

    def main(self):
        # reading raw data from the sensorboard
        # has to go to a thread later
        bus = BusFactory.produceSerialTransceiver()
        bus.readBusUntilStopFlag(self.someMethod)