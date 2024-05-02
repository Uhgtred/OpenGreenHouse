#!/usr/bin/env python3
# @author: Markus Kösters
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Sensor(Protocol):
    """
    Dataclass for prescribing the structure of a Sensor-object.
    """
    type: str
    id: int
    value: any
