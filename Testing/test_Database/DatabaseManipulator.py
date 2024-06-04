#!/usr/bin/env python3
# @author: Markus Kösters
import os.path
import sqlite3
import unittest
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class dummyDataBase(DatabaseInterface):

    _name = 'DataBaseFiles/dummyDatabase.db'
    _tableName = 'dummyDatabase'

    def connect(self) -> Connection:
        return sqlite3.connect(self._name)

    def close(self, connection: any) -> None:
        pass

    @property
    def name(self) -> str:
        pass

    def createTable(self, connection: any, tableName: str) -> any:
        if tableName:
            tableHandle.execute(f'CREATE TABLE IF NOT EXISTS {tableName}')
        else:
            tableHandle.execute(f'CREATE TABLE IF NOT EXISTS {self._tableName}')

    def createTableHandle(self, connection: any) -> object:
        pass

    def insertData(self, data: tuple, tableHandle: any) -> None:
        pass

    def getData(self, tableHandle: any) -> list[tuple]:
        pass

    def getDataByKeyWord(self, column: str, keyWord: str, tableHandle: any) -> list[tuple]:
        pass


class test_DataBaseManipulator(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseManipulator(dummyDataBase)

    def test_connect(self):
        self.database.connect()
        self.assertTrue(os.path.exists(dummyDataBase._name))

    def test_connectFileAlreadyExists(self):
        self.assertTrue(os.path.exists(dummyDataBase._name))
        self.database.connect()
        self.assertTrue(os.path.exists(dummyDataBase._name))

    def test_disconnect(self):
        self.database.disconnect()

    def test_createTable(self):
        self.database.createTable('test')

if __name__ == '__main__':
    unittest.main()
