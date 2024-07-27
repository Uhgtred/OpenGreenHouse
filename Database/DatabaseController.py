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

    def openDatabase(self, database: DatabaseInterface) -> None:
        """
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        Only opens a connection to a database when there is not an existing instance with the same name yet.
        :param database: Database instance that will be opened.
        """
        if not any(database.name in item for item in self.__databaseInstances):
            databaseManipulator = DatabaseManipulator(database)
            databaseManipulator.connect()
            self.__databaseInstances.add(databaseManipulator)

    def closeDatabase(self, database: DatabaseInterface) -> None:
        """
        Method for closing a specific database instance.
        :param database: Name of the database that will be closed.
        """
        for databaseInstance in self.__databaseInstances:
            if database.name == databaseInstance.databaseName:
                databaseInstance.disconnect()
                self.__databaseInstances.remove(databaseInstance)
                break

    def __closeAllDatabases(self) -> None:
        """
        Method for closing all database instances.
        """
        for databaseInstance in self.__databaseInstances:
            databaseInstance.disconnect()
