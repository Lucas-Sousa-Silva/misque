FROM python:3.10.2-slim-bullseye AS base

#Copy requeriments
WORKDIR /opt/app
COPY requeriments.txt /opt/app

# Install python dependencies
WORKDIR /opt/app
RUN pip3 install -r requeriments.txt

# # Copy backend project
# COPY src/backend /opt/app
# EXPOSE 8000
# ENTRYPOINT python3 -m uvicorn main:app
