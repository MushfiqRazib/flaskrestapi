#FROM ubuntu:16.04

# Using lightweight alpine image
FROM python:3.7.1-alpine

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

WORKDIR /project

#RUN apt-get update -y && \
    #apt-get install -y python-pip python-dev

RUN pip install --no-cache-dir pipenv

ADD . /project

#RUN pip install --upgrade pip

COPY ./requirements.txt /project/requirements.txt

#RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

#CMD flask run --host=0.0.0.0

RUN chmod +x entry.sh

ENTRYPOINT ["/bin/sh", "./entry.sh"]