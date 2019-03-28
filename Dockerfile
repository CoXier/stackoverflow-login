FROM python:3.7.2-alpine3.9
LABEL maintainer="hi@harryyu.me"


ENV APPPATH /app
COPY . ${APPPATH}
WORKDIR ${APPPATH}

RUN chmod 755 ${APPPATH}/dev_script/crontab \
  && chmod 755 ${APPPATH}/dev_script/entry.sh \
  && chmod 755 ${APPPATH}/dev_script/robot.sh \
  && /usr/bin/crontab ${APPPATH}/dev_script/crontab \
  && pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "$APPPATH/dev_script/entry.sh"]