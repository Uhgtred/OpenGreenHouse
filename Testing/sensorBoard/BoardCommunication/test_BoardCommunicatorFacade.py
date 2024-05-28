#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from sensorBoard.BoardCommunication.BoardCommunicatorFacade import BoardCommunicatorFacade
from sensorBoard.BoardCommunication.BoardCommunicatorFacadeFactory import BoardCommunicatorFacadeFactory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.facade = BoardCommunicatorFacadeFactory.produceBoardCommunicatorFacade()

    def test_readSensorData(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
