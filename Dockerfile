+FROM python:3.9.5-alpine

RUN apk update && apk upgrade
RUN apk --no-cache add gcc libc-dev libxml2-dev libxslt-dev
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
