# Create docker file
FROM ubuntu:18.04

# This is the name of company
MAINTAINER RecylaBox

# Install python3.8 version
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3.8 \
	python3-pip \
	python3-setuptools \
	python3-virtualenv \
	python3-virtualenvwrapper \
	git \
	&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN python3 -m virtualenv --python=/usr/bin/python3 /opt/venv

# Upgrade pip3 when is may need it
RUN pip3 install --upgrade pip

# Create folder for the project
RUN mkdir /project
WORKDIR /project

# Add the current folder include code to working dir
ADD . /project/

# this is tell the user for the linux not be root
RUN adduser -D dilshad
USER dilshad

#Set default enviroment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninterative

# Set project enviroment variables
# Grab these via Python's os.environ
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get in

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# To run dockerfile (docker build -t ecomma -f Dockerfile .)
