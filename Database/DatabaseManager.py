#!/usr/bin/env python3
# @author: Markus Kösters
import os
from pathlib import Path
import pathlib

from Database.DatabaseInterface import DatabaseInterface
from Database.DatabaseManipulator import DatabaseManipulator


class DatabaseManager:

    __dataBaseManipulators: list[DatabaseManipulator]

    def __init__(self):
        pass

    def createNewDatabase(self, databaseName: str, databaseType: DatabaseInterface):
        self.__createDatabaseFile(databaseName)
        self.__dataBaseManipulators.append(DatabaseManipulator(databaseType))

    def __createDatabaseFile(self, databaseName: str):

        os.makedirs(Path(os.path.dirname(__name__)).parent(), exist_ok=True)
        