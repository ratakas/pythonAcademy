FROM python:3-onbuild
RUN apt-get -y update \
	&& apt-get -y install cron
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
ADD crontab /etc/cron.d/simple-cron
RUN touch /var/log/cron.log
CMD ['cron']
