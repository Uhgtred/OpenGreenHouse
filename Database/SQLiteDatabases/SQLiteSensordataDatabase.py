#!/usr/bin/env python3
# @author: Markus Kösters

import sqlite3
from sqlite3 import Connection

from Database.DatabaseInterface import DatabaseInterface


class SQLiteSensordataDatabase(DatabaseInterface):
    """
    The SQLiteSensordataDatabase class is used to store the sensor data in.
    """

    __name = 'SensorData.db'
    __tableName = 'SensorData'
    # Todo: prescribe the format of the table.
    __tableFormat = ()

    def connect(self) -> Connection:
        """
        Connects to the database.
        :return: Connection instance object.
        """
        return sqlite3.connect(self.__name)

    def close(self, connection: Connection) -> None:
        """
        Method for closing the connection to the database.
        """
        connection.close()

    @property
    def name(self) -> str:
        """
        Property for getting the name of the database.
        :return: Name of the database.
        """
        return self.__name

    def createTableHandle(self, connection: Connection) -> Connection.cursor:
        """
        Method for creating the database table-handle.
        :param connection: Connection instance upon which the table-handle will be created.
        :return: Table handle instance.
        """
        cursor = connection.cursor()
        return cursor

    def createTable(self, tableHandle: Connection.cursor) -> None:
        """
        Method for creating a table.
        :param tableName: Name of the table that will be created.
        :param tableHandle: Object to create the table upon.
        """
        tableHandle.execute(f'CREATE TABLE IF NOT EXISTS {self.__tableName} {self.__tableFormat}')

    def insertData(self, data: tuple, tableHandle: Connection.cursor) -> None:
        """
        Method for inserting data into the database.
        :param tableName: Name of the table that the data will be inserted in.
        :param data: Data to be inserted into the database.
        :param tableHandle: Handle that will be used to insert the data into the database.
        """
        tableHandle.executemany(f'INSERT INTO {self.__tableName} VALUES(?,?,?)', data)

    def getData(self, tableHandle: any) -> list[tuple]:
        """
        Method for getting data from the database.
        :param tableHandle: Name of the table that the data will be read from.
        :return: List of tuples containing the data from the database.
        """
        tableContent = []
        for row in tableHandle.execute(f'select * from {self.__tableName}'):
            tableContent.append(row)
        return tableContent
