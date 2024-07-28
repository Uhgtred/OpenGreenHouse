#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from Database.DatabaseController import DatabaseController
from Database.DatabaseManipulator import DatabaseManipulator
from Testing.test_Database.StubsAndMocks.dummyDatabase import dummyDataBase


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.databaseController = DatabaseController()

    def test_openDatabase(self) -> None:
        """
        Method for testing the Opening of the database by the database-controller.
        """
        self.databaseController.openDatabase(dummyDataBase)
        assert isinstance(list(self.databaseController._DatabaseController__databaseInstances)[0], DatabaseManipulator)
        self.databaseController.closeDatabase(dummyDataBase)

    def test_closeDatabase(self) -> None:
        """
        Method for testing the Closing of the database by the database-controller.
        """
        self.databaseController.openDatabase(dummyDataBase)
        self.databaseController.closeDatabase(dummyDataBase)
        self.assertListEqual([], list(self.databaseController._DatabaseController__databaseInstances))


if __name__ == '__main__':
    unittest.main()
