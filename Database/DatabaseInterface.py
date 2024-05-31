#!/usr/bin/env python3
# @author: Markus Kösters

from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    """
    Interface for database operations. The specific database operations will be defined in a class inheriting from this interface.
    """

    @abstractmethod
    def connect(self) -> type:
        """
        Connects to the database
        :return:
        """

    @abstractmethod
    def close(self, connection: any) -> None:
        """
        Closes the connection to the database
        """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Interface getter method for the name of the database.
        :return str: Name of the database.
        """

    @abstractmethod
    def createTable(self, connection: any) -> any:
        """
        Interface method for creating a table.
        :param connection: Connection instance of the database.
        """

    @abstractmethod
    def createTableHandle(self, connection: any) -> object:
        """
        Interface method for creating a table handle.
        :param connection: Connection instance on which the table-handle will be created.
        :return: Connection instance on which the table-handle will be created.
        """

    @abstractmethod
    def insertData(self, data: tuple, tableHandle: any) -> None:
        """
        Interface method for inserting data to the table.
        :param data: Data to be inserted.
        :param tableHandle: Table handle instance.
        """

    @abstractmethod
    def getData(self, tableHandle: any) -> tuple:
        """
        Interface method for getting data from the table.
        :param tableHandle: Table handle instance.
        :return: Data from the table.
        """
