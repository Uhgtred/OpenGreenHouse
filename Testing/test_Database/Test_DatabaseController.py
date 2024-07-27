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
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        Todo: implement
        """
        self.databaseController.openDatabase(dummyDataBase())
        print(list(self.databaseController._DatabaseController__databaseInstances)[0])
        self.assertIn(DatabaseManipulator, list(self.databaseController._DatabaseController__databaseInstances))

    def test_closeDatabase(self) -> None:
        """
        Method for closing a specific database instance.
        Todo: implement
        """
        pass

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
