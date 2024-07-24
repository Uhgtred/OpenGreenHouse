#!/usr/bin/env python3
# @author: Markus Kösters
import atexit

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class DatabaseController:

    __databaseInstances: set[dict[str, DatabaseManipulator]]

    def __init__(self):
        # Closing all databases when the program is being closed!
        atexit.register(self.__closeAllDatabases)

    def openDatabase(self, databaseName: str, database: DatabaseInterface) -> None:
        """
        Method for opening the database and keep an instance as long as the instance is not actively being closed.
        Only opens a connection to a database, when there is not yet an existing instance with the same name.
        :param databaseName: Name of the database that will be opened.
        :param database: Database instance that will be opened.
        """
        if not any(databaseName in dict(item) for item in self.__databaseInstances):
            databaseManipulator = DatabaseManipulator(database)
            databaseManipulator.connect()
            self.__databaseInstances.add({databaseName: databaseManipulator})

    def closeDatabase(self, databaseName: str) -> None:
        """
        Method for closing a specific database instance.
        :param databaseName: Name of the database that will be closed.
        """
        for databaseDictionary in self.__databaseInstances:
            for databaseName, databaseManipulatorInstance in databaseDictionary.items():
                if databaseName == databaseName:
                    databaseManipulatorInstance.disconnect()
                    self.__databaseInstances.remove({databaseName: databaseManipulatorInstance})

    def __closeAllDatabases(self) -> None:
        """
        Method for closing all database instances.
        """
        for databaseDictionary in self.__databaseInstances:
            list(databaseDictionary.values())[0].disconnect()
