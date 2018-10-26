FROM python:3.6-alpine

RUN adduser -D microblog
RUN apk update
RUN apk add --no-cache binutils
RUN apk add --no-cache gcc
RUN apk add --no-cache musl-dev
RUN apk add --no-cache mariadb-dev
RUN apk add --no-cache mariadb-client
RUN apk add --no-cache mysql-client

ENV PYTHONUNBUFFERED 1

RUN pip install mysqlclient
WORKDIR /home/bfcrudassign

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN venv/bin/pip install setuptools
RUN venv/bin/pip install PyMySQL


COPY app app
COPY migrations migrations
COPY bfcrudassign.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R bfcrudassign:bfcrudassign ./
USER bfcrudassign

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]