#!/usr/bin/env python3
# @author Markus Kösters
import pickle
from typing import Protocol


class EncodingProtocol(Protocol):
    """
    Protocol for prescribing the structure of the encoding.
    """

    @staticmethod
    def decode(message: any) -> any:
        """
        Method for decoding a message received from a bus.
        :param message: Message from bus that needs to be decoded.
        """
        pass

    @staticmethod
    def encode(message: any) -> any:
        """
        Method for encoding a message that will be sent to a bus.
        :param message: Message that needs to be encoded.
        """
        pass


class ArduinoSerialEncoding(EncodingProtocol):
    """
    Protocol for prescribing the structure of the encoding.
    """

    @staticmethod
    def decode(message: any) -> str:
        """
        Method for decoding a message received from a bus.
        :param message: Message from bus that needs to be decoded.
        """
        if not message:
            return None
        if isinstance(message, bytes):
            message = message.decode()
        if message.endswith('&'):
            message = message[:-1]
        return message

    @staticmethod
    def encode(message: str) -> bytes:
        """
        Method for encoding a message that will be sent to a bus.
        :param message: Message that needs to be encoded.
        """
        if not isinstance(message, bytes):
            message = f'{message}&'.encode()
        return message


class SocketEncoding(EncodingProtocol):

    @staticmethod
    def decode(message: any) -> str:
        """
        Method for decoding a message received from a socket.
        :param message: Message from socket that needs to be decoded.
        """
        if isinstance(message, bytes):
            message = message.decode()
        return message

    def encode(self, message: str) -> bytes:
        """
        Method for encoding a message that will be sent to a socket.
        :param message: Message that needs to be encoded.
        """
        if not isinstance(message, bytes):
            return message.encode()
        return message


class SocketEncodingPickle(EncodingProtocol):

    @staticmethod
    def decode(message: any) -> str:
        """
        Method for decoding a message received from a socket.
        :param message: Message from socket that needs to be decoded.
        """
        if isinstance(message, bytes):
            message = pickle.loads(message)
        return message

    def encode(self, message: str) -> bytes:
        """
        Method for encoding a message that will be sent to a socket.
        :param message: Message that needs to be encoded.
        """
        if not isinstance(message, bytes):
            return pickle.dumps(message)
        return message
