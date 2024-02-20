#!/usr/bin/python3
"""Defines a JSON to object function."""
import json


def from_json_string(my_str):
    """Returns an object Python represented by a JSON string."""
    return json.loads(my_str)
