#!/usr/bin/env python

from uuid import UUID, uuid4


# Create a dictionary to keep things in memory
_in_memory_storage = dict()


# Save received data in memory giving an uuid
def save(data):
    data_uuid = uuid4()

    _in_memory_storage[data_uuid] = data

    return data_uuid


def get(uuid):
    return _in_memory_storage[UUID(uuid)]
