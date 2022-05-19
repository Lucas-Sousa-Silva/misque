FROM python:3.10.2-slim-bullseye AS base

# Copy requeriments
WORKDIR /opt/app
COPY requeriments.txt /opt/app

# Disable creating __pycache__ directories
ENV PYTHONDONTWRITEBYTECODE=1

# Install python dependencies
WORKDIR /opt/app
RUN pip3 install -r requeriments.txt

