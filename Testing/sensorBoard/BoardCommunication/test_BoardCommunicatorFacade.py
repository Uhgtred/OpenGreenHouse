#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from sensorBoard.BoardCommunication.BoardCommunicatorFacadeFactory import BoardCommunicatorFacadeFactory


def stubSensorReaderMethod(someMessage):
    return 'test'

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.facade = BoardCommunicatorFacadeFactory.produceBoardCommunicatorFacade(stub=True, sensorReaderMethod=stubSensorReaderMethod)

    def test_readSensorData(self):
        test = self.facade.readSensorData
        print(test)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
