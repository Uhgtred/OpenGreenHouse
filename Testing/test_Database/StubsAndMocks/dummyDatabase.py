#!/usr/bin/env python3
# @author: Markus Kösters
import os
import sqlite3
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface


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
