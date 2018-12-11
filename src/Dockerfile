FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ADD . /code/