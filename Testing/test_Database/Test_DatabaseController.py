#!/usr/bin/env python3
# @author: Markus Kösters

import unittest

from Database.DatabaseController import DatabaseController


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.databaseController = DatabaseController()

    def test_openDatabase(self) -> None:
        """
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        Todo: implement
        """
        databaseName = 'dummyDatabase'
        self.databaseController.openDatabase(databaseName,'Testing/test_Database/DataBaseFiles/dummyDatabase')

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
