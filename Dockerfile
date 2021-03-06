# Pull python base image
FROM python:3.7.4-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installing requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && pip install pylint-django


# Copy Project to the container
RUN mkdir -p /fyle-qbo-api
COPY . /fyle-qbo-api/
WORKDIR /fyle-qbo-api

# Do linting checks
RUN pylint --load-plugins pylint_django --rcfile=.pylintrc **/**.py

# Expose development port
EXPOSE 8000

# Run development server
CMD /bin/bash run.sh
