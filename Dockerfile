FROM python:3

ENV PATH /app
COPY . ${PATH}
WORKDIR ${PATH}

# cron setting from https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
RUN apt-get -y install cron
ADD ./dev_script/crontab /etc/cron.d/schedule-contab
RUN chmod 0644 /etc/cron.d/schedule-contab
RUN crontab /etc/cron.d/schedule-contab