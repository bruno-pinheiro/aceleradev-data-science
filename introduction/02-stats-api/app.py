#!/usr/bin/env python

from flask import Flask, request, jsonify
from loguru import logger

from statsapi import data_store
from statsapi import operation

app = Flask(__name__)

# Creating an endpoint to send data
@app.route("/data", methods=["POST"])
def save_data():
    # setting log for this action
    logger.info(f"Saving data...")

    # transform content requisition to json
    content = request.get_json()

    # save in a module just the "data" field
    # The uuid of the data
    uuid = data_store.save(content["data"])

    # set log for las action
    logger.info(f"Data saved with UUID '{uuid}' successfully")

    # define information to be returned
    return jsonify({"status": "success",
                    "message": "data saved successfully",
                    "uuid": uuid})


# Creating an endpoint to get data
@app.route("/data/<uuid>", methods=["GET"])
def retrieve_data(uuid):
    logger.info(f"Retrieving data associated with UUID '{uuid}'...")

    try:
        stored_data = data_store.get(uuid)
    except KeyError:
        logger.warning(f"Cannot retrieve data associated with UUID '{uuid}'")

        return jsonify({"status": "failed",
                        "message": "data cannot be retrieved",
                        "data": []})

    logger.info(f"Data associated with UUID '{uuid}' retrieved successfully")

    return jsonify({"status": "success",
                    "message": "data retrieved successfully",
                    "data": stored_data})


# Creating an endpoint to operate on date
@app.route("/data/<uuid>/<operation>", methods=["GET"])
def process_operation(uuid, operation):
    logger.info(f"Processing operation '{operation}' on data associated with UUID '{uuid}'...")

    try:
        stored_data = data_store.get(uuid)

        operation_func = get_operation(operation)

        result = operation_func(stored_data)

    except KeyError:
        logger.warning(f"Cannot retrieve data associated with UUID '{uuid}'")

        return jsonify({"status": "failed",
                        "message": "data cannot be retrieved",
                        "result": None})

    except NoSuchOperationError:
        logger.warning(f"Cannot find operation '{operation}'")

        return jsonify({"status": "failed",
                        "message": f"no such operation '{operation}'",
                        "result": None})

    logger.info(f"Operation '{operation}' on data associated with UUID '{uuid}' finished successfully")

    return jsonify({"status": "success",
                    "message": "result completed",
                    "result": result})


class NoSuchOperationError(Exception):
    pass


def get_operation(operation_name):
    if operation_name == "min":
        return operation.op_min
    if operation_name == "max":
        return operation.op_max
    if operation_name == "mean":
        return operation.op_mean
    else:
        NoSuchOperationError


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
