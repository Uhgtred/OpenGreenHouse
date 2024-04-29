#!/usr/bin/env python3
# @author: Markus Kösters

from flask import jsonify, Response
from flask_restful import Resource


class RequestActorControl(Resource):
    """
    Class for pushing a request for actor control.
    """

    def set(self, actor, value: int) -> Response:
        actorContol.set(actor, value)
        return Response

