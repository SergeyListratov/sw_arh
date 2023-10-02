# pull official base image
FROM python:3.11.3-slim-buster
#FROM python:3.9-slim-bookworm

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV FLASK_APP=manage
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
