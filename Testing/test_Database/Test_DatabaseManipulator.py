#!/usr/bin/env python3
# @author: Markus Kösters

import os.path
import sqlite3
import unittest
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator
from Testing.test_Database.StubsAndMocks.dummyDatabase import dummyDataBase


class test_DataBaseManipulator(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseManipulator(dummyDataBase())

    def test_connect(self):
        self.database.connect()
        self.assertTrue(os.path.exists(dummyDataBase._name))
        self.assertIsNotNone(self.database._DatabaseManipulator__databaseConnection)
        self.database.disconnect()

    def test_connectFileAlreadyExists(self):
        self.assertTrue(os.path.exists(dummyDataBase._name))
        self.database.connect()
        self.assertTrue(os.path.exists(dummyDataBase._name))
        self.database.disconnect()

    def test_insertData(self):
        self.database.connect()
        self.database.insertData(('1234', '56789'))
        self.assertIn(('1234', '56789'), self.database.getData())
        self.database.disconnect()

    def test_disconnect(self):
        self.database.connect()
        self.database.disconnect()
        self.assertIsNone(self.database._DatabaseManipulator__databaseConnection)

    def test_createTable(self):
        self.database.connect()
        self.database.createTable(('testcolumn', 'testcolumn2'), 'test')
        connection = sqlite3.connect(os.path.join('DataBaseFiles', 'dummyDatabase'))
        cursor = connection.cursor()
        listOfTables = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='test'; """).fetchall()
        self.assertIn(('test',), listOfTables)
        self.database.disconnect()

    def test_getDataByKeyWord(self):
        self.database.connect()
        self.assertIn(('1234', '56789'), self.database.getDataByKeyWord('test', '1234'))
        self.assertNotIn(('1234', '56789'), self.database.getDataByKeyWord('test', '56789'))
        self.database.disconnect()

    def test_getData(self):
        self.database.connect()
        self.assertIn(('1234', '56789'), self.database.getData())
        self.database.disconnect()


if __name__ == '__main__':
    unittest.main()
    os.remove(os.path.join('Testing', 'test_Database', 'DataBaseFiles', 'dummyDatabase'))
