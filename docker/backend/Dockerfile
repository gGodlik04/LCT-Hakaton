# pull official base image
FROM python:3.11

# set work directory
WORKDIR /srv/www/Backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./Backend  /srv/www/Backend
RUN pip install -r requirements.txt