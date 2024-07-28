#!/usr/bin/env python3
# @author: Markus Kösters

import atexit

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class DatabaseController:

    __databaseInstances: set[DatabaseManipulator] = set()

    def __init__(self):
        # Closing all databases when the program is being closed!
        atexit.register(self.__closeAllDatabases)

    def openDatabase(self, database: DatabaseInterface | type(DatabaseInterface)) -> None:
        """
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        Only opens a connection to a database when there is not an existing instance with the same name yet.
        :param database: Database instance that will be opened.
        """
        database: DatabaseInterface = self.__checkCallable(database)
        if not any(database.name == item.databaseName for item in self.__databaseInstances):
            databaseManipulator = DatabaseManipulator(database)
            databaseManipulator.connect()
            self.__databaseInstances.add(databaseManipulator)

    def closeDatabase(self, database: DatabaseManipulator | type(DatabaseManipulator)) -> None:
        """
        Method for closing a specific database instance.
        :param database: Name of the database that will be closed.
        """
        database = self.__checkCallable(database)
        database = self.__findDatabase(database)
        database.disconnect()
        self.__databaseInstances.remove(database)

    def writeToDatabase(self, database: DatabaseManipulator | type(DatabaseManipulator), data: tuple) -> None:
        """
        Method for w
        :param database:
        :param data: Data that will be written to the database
        """
        database: DatabaseManipulator = self.__findDatabase(database)
        database.insertData(data)

    def __findDatabase(self, database: DatabaseManipulator | type(DatabaseManipulator)) -> DatabaseManipulator:
        """
        Method for finding the database by name.
        :param database: Database name that is being searched for.
        :return: DatabaseManipulator instance that contains the database.
        """
        for databaseInstance in self.__databaseInstances:
            if databaseInstance.databaseName == database.name:
                return databaseInstance

    @staticmethod
    def __checkCallable(object_: any) -> DatabaseManipulator | DatabaseInterface:
        """
        Static method for checking if the object is callable.
        :param object_: Object to be checked.
        :return: Instance of the object if callable, otherwise the Object.
        """
        if callable(object_):
            return object_()
        return object_

    def __closeAllDatabases(self) -> None:
        """
        Method for closing all database instances.
        """
        for databaseInstance in self.__databaseInstances:
            databaseInstance.disconnect()
