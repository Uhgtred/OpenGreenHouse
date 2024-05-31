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
    def close(self) -> None:
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