#!/usr/bin/env python3
# @author: Markus Kösters

import os.path
import sqlite3
import unittest
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class dummyDataBase(DatabaseInterface):

    _name = os.path.join('DataBaseFiles', 'dummyDatabase')
    _tableName = 'dummyDatabase'

    def __init__(self):
        self.tableHandle = None

    def connect(self) -> Connection:
        return sqlite3.connect(self._name)

    def close(self, connection: any) -> None:
        connection.close()

    @property
    def name(self) -> str:
        return self._name

    def createTable(self, tableHandle: Connection.cursor, columns: tuple, tableName: str = None) -> any:
        if tableName:
            tableHandle.execute(f'CREATE TABLE IF NOT EXISTS {tableName} {columns}')
        else:
            tableHandle.execute(f'CREATE TABLE IF NOT EXISTS {self._tableName} {columns}')

    def createTableHandle(self, connection: any) -> object:
        cursor = connection.cursor()
        return cursor

    def insertData(self, data: tuple, tableHandle: any) -> None:
        tableHandle.execute(f'INSERT INTO {self._tableName} VALUES{data}')

    def getData(self, tableHandle: any) -> list[tuple]:
        tableContent = []
        for row in tableHandle.execute(f'select * from {self._tableName}'):
            tableContent.append(row)
        return tableContent

    def getDataByKeyWord(self, column: str, keyWord: str, tableHandle: any) -> list[tuple]:
        tableHandle.execute(f'select * from {self._tableName} where {column} like "%{keyWord}%"')
        filteredTableContent = tableHandle.fetchall()
        return filteredTableContent

    def saveChanges(self, connection: Connection) -> None:
        connection.commit()


class test_DataBaseManipulator(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseManipulator(dummyDataBase)

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
