#!/usr/bin/env python

import requests


def send(data):
    response = requests.post("http://localhost:5000/data", json={"data": data})

    print(response.json())


def main():
    send([1, 2, 3, 4])


if __name__ == "__main__":
    main()
