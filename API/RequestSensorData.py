#!/usr/bin/env python3
# @author: Markus Kösters

from flask import jsonify, Response
from flask_restful import Resource

from SensorReader.SensorReaderInterface import SensorReaderInterface


class RequestSensorData(Resource):
    """
    Class to request sensor data.
    """
    __sensorReader: SensorReaderInterface = None

    def __init__(self, sensorReaderInstance: SensorReaderInterface):
        self.__sensorReader = sensorReaderInstance

    def get(self) -> Response:
        """
        Method for getting sensor-data from the sensorBoard.
        :return: List containing all sensor data.
        """
        if self.__sensorReader:
            sensorValues = self.__sensorReader.readSensorData()
            # returning sensorValues that have been read from the sensorBoard
            return jsonify(sensorValues)
        else:
            raise BaseException('No instance of SensorReader found. Please instance this class with a valid Instance of the SensorReader Class!')
