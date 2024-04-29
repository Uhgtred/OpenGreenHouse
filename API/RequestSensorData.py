#!/usr/bin/env python3
# @author: Markus Kösters

from flask import jsonify, Response
from flask_restful import Resource


class RequestSensorData(Resource):
    """
    Class to request sensor data.
    """

    def get(self) -> Response:
        """
        Method for getting sensor-data from the sensorBoard.
        :return: List containing all sensor data.
        """
        sensorValues = sensorReader.getSensorValues()
        # returning sensorValues that have been read from the sensorBoard
        return jsonify(sensorValues)
