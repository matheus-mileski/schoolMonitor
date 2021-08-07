FROM python:3.8
LABEL authors="Matheus Mileski, Julio Ribeiro"

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y \
        python3-gdal \
        libgeos++-dev \
        libproj-dev \
        openjdk-11-jdk \
        vim \
        htop \
        wait-for-it \
        binutils \
        libproj-dev \
        gdal-bin \
        gettext

RUN addgroup -q django && \
    adduser --quiet --ingroup django --disabled-password django

RUN mkdir /api

WORKDIR /api

COPY requirements.txt /requirements.txt

COPY entrypoint.sh /entrypoint.sh

USER django

ENV PATH=/home/django/.local/bin:$PATH

RUN pip install -r /requirements.txt

