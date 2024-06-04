#!/usr/bin/env python3
# @author: Markus Kösters
from Database.DatabaseInterface import DatabaseInterface


class DatabaseManipulator:
    """
    Class for setting up a Database instance and managing access to the database.
    """

    def __init__(self, database: DatabaseInterface):
        if callable(database):
            self.__dataBaseInstance: DatabaseInterface = database()
        else:
            self.__dataBaseInstance: DatabaseInterface = database
        self.__databaseConnection: object = None
        self.__tableHandle: object = None

    def connect(self) -> None:
        """
        Method to connect to the database.
        """
        self.__databaseConnection: object = self.__dataBaseInstance.connect()
        self.__tableHandle: object = self.__dataBaseInstance.createTableHandle(self.__databaseConnection)

    def disconnect(self) -> None:
        """
        Method to disconnect from the database.
        """
        self.__dataBaseInstance.close(self.__databaseConnection)
        self.__tableHandle: object = None
        self.__databaseConnection: object = None

    def createTable(self, tableName: str = None) -> None:
        """
        Method to create a new table.
        :param tableName: Name of the table. None means that the table-name will be the same as the file-name.
        """
        self.__dataBaseInstance.createTable(self.__databaseConnection, tableName)

    def insertData(self, data: tuple) -> None:
        """
        Method to insert data into an existing table.
        :param data: Data to be inserted.
        """
        self.__dataBaseInstance.insertData(data, self.__tableHandle)

    def getData(self) -> list[tuple]:
        """
        Method to retrieve data from the table.
        :return: List of tuples containing the data of the database.
        """
        return self.__dataBaseInstance.getData(self.__tableHandle)

    def getDataByKeyWord(self, column: str, keyWord: str) -> list[tuple]:
        return self.__dataBaseInstance.getDataByKeyWord(column, keyWord, self.__tableHandle)
