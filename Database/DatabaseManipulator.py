#!/usr/bin/env python3
# @author: Markus Kösters
from Database.DatabaseInterface import DatabaseInterface


class DatabaseManipulator:
    """
    Class for setting up a Database instance and managing access to the database.
    """

    def __init__(self, database: DatabaseInterface):
        self.__dataBaseInstance: DatabaseInterface = database
        self.__databaseConnection: DatabaseInterface

    def connect(self) -> None:
        """
        Method to connect to the database.
        :param database: Database that will be connected to.
        :return: Instance of the Database.
        """
        self.__databaseConnection = self.__dataBaseInstance.connect()

    def disconnect(self) -> None:
        """
        Method to disconnect from the database.
        """
        self.__dataBaseInstance.close(self.__databaseConnection)




