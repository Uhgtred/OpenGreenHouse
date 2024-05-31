#!/usr/bin/env python3
# @author: Markus Kösters

from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

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
    def createTable(self, tableName: str, connection: any) -> any:
        """
        Interface method for creating a table.
        """

    @abstractmethod
    def createTableHandle(self, connection: any) -> object:
        """
        Interface method for creating a table handle.
        :param connection: Connection instance on which the table-handle will be created.
        :return: Connection instance on which the table-handle will be created.
        """

    @abstractmethod
    def insertData(self, tableName: str, data: tuple, tableHandle: any) -> None:
        """
        Interface method for inserting data to the table.
        :param tableName:
        :param data:
        :param tableHandle:
        :return:
        """
