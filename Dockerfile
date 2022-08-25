# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/car_house

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFsFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev