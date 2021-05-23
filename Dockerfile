FROM python:3.9.5-alpine

RUN apk update && apk upgrade && apk --no-cache add gcc libc-dev libxml2-dev libxslt-dev
WORKDIR /server/
COPY ./config/requirements.txt /server
RUN pip install -r requirements.txt
COPY . /server/