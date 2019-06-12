# `[Flask API example]`

This is a simple example of an API created with Flask framework in Python.

It contains endpoints to send, retrieve and operate on data
stored in the API.

Simple operations like min, max and mean are embedded.

## Usage

Download this project folder and goes to there.

### 1. Create an environment with the required configuration, present in requirements.txt:

```bash
$ conda create --name myenv --file requirements.txt python=3.7
```

Then activate the environement:

```bash
$ conda activate myenv
```

### 2. Run the app in the terminal

```bash
$ python app.py
```

### 3. Interact with the API

Let the app running and open another terminal session. On this new terminal

**It's possible to send data**

```bash
$ python client.py --send --data "[1, 2, 3, 4]"
```

The data will be identified by an UUID, which will be displayed.

**It's possible to retrieve data**

Use the sent data uuid to retrieve stored data:

```bash
$ python client.py --get --uuid "<put_here_the_uuid>"
```

**And it's possible to operate on data**

```bash
$ python client.py --calc op min --uuid "<put_here_the_uuid>"

$ python client.py --calc op max --uuid "<put_here_the_uuid>"

$ python client.py --calc op mean --uuid "<put_here_the_uuid>"
```
