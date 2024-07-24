#!/usr/bin/env python3
# @author: Markus Kösters
import atexit

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class DatabaseController:

    __databaseInstances: set[dict[str, DatabaseManipulator]]

    def __init__(self):
        atexit.register(self.__closeAllDatabases())


    def openDatabase(self, databaseName: str, database: DatabaseInterface):
        """
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        :param databaseName:
        :param database:
        :return:
        """
        if not any(databaseName in dict(item) for item in self.__databaseInstances):
            databaseManipulator = DatabaseManipulator(database)
            databaseManipulator.connect()
            self.__databaseInstances.add({databaseName: databaseManipulator})

    def __closeAllDatabases(self) -> None:
        """
        Method for closing all database instances.
        """
        for databaseInstance in self.__databaseInstances:
            for databaseName, databaseManipulator in databaseInstance.items():
                databaseManipulator.disconnect()