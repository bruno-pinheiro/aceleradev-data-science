#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route('/users/<string:username>')
def hello_world(username=None):

	return "Hello {}!".format(username)
