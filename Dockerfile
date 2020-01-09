FROM python:3.7-alpine

RUN apk update && \
    apk add gcc g++ libc-dev && \
    apk add python3-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000