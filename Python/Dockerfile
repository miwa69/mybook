FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
