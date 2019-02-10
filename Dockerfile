FROM ubuntu:latest
MAINTAINER fnndsc "hi@harryyu.me"

ENV APPPATH /app
COPY . ${APPPATH}
WORKDIR ${APPPATH}

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get install -y cron \
  && pip install -r requirements.txt

ADD ./dev_script/crontab /etc/cron.d/schedule-contab
RUN chmod 0644 /etc/cron.d/schedule-contab \
  && crontab /etc/cron.d/schedule-contab