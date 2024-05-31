#!/usr/bin/env python3
# @author: Markus Kösters
from Database.DatabaseInterface import DatabaseInterface


class DatabaseManipulator:

    def __init__(self):
        self.__database: DatabaseInterface = None

    def connect(self, database: DatabaseInterface) -> type:
        """
        Method to connect to the database.
        :param database: Database that will be connected to.
        :return: Instance of the Database.
        """
        self.__database = database.connect(database.name)

