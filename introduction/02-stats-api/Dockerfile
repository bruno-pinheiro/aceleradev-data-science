FROM python:3.7-alpine

RUN apk update
RUN apk add openssl-dev
RUN apk add gcc musl-dev libffi-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /statsapi
RUN mkdir /logs

COPY ./app.py /app.py
COPY ./statsapi/data_store.py /statsapi/data_store.py
COPY ./statsapi/operation.py /statsapi/operation.py

EXPOSE 5000

CMD python app.py
