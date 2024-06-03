#!/usr/bin/env python3
# @author: Markus Kösters
from Database.DatabaseInterface import DatabaseInterface


class DatabaseManipulator:
    """
    Class for setting up a Database instance and managing access to the database.
    """

    def __init__(self, database: DatabaseInterface):
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

    def createTable(self) -> None:
        """
        Method to create a new table.
        :return:
        """
        self.__dataBaseInstance.createTable(self.__databaseConnection)

    def insertData(self, data: tuple) -> None:
        """
        Method to insert data into an existing table.
        :param data: Data to be inserted.
        """
        self.__dataBaseInstance.insertData(data, self.__tableHandle)

    def getData(self) -> tuple:
        """
        Todo: some information about the data that shall be extracted from the database.
        Method to retrieve data from the table.
        :return: Tuple containing the data of the database.
        """






