#!/usr/bin/env ṕython

from flask import Flask, request, jsonify
from loguru import logger

from statsapi import data_store


app = Flask(__name__)


# Creating an endpoint
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
    logger.info(f"Data saved with UUID `{uuid}` successfully")

    # define information to be returned
    return jsonify({"status": "success",
                    "message": "data saved successfully",
                    "uuid": uuid})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
