FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get --assume-yes update &&\
    apt-get --assume-yes install pkg-config python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn main:app --host=0.0.0.0 --reload
