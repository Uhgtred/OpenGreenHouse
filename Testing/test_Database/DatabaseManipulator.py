#!/usr/bin/env python3
# @author: Markus Kösters
import sqlite3
import unittest
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface


class dummyDataBase(DatabaseInterface):
    __name = 'DataBaseFiles/dummyDatabase.db'
    __tableName = 'dummyDatabase'

    def connect(self) -> Connection:
        return sqlite3.connect(self.__name)

    def close(self, connection: any) -> None:
        pass

    @property
    def name(self) -> str:
        pass

    def createTable(self, connection: any) -> any:
        pass

    def createTableHandle(self, connection: any) -> object:
        pass

    def insertData(self, data: tuple, tableHandle: any) -> None:
        pass

    def getData(self, tableHandle: any) -> list[tuple]:
        pass

    def getDataByKeyWord(self, column: str, keyWord: str, tableHandle: any) -> list[tuple]:
        pass


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.database = dummyDataBase()

    def test_connect(self):
        print(self.database.connect())
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
