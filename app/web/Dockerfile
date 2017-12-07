FROM python:3-onbuild
RUN apt-get update
COPY requirements.txt /usr/src/api/
RUN pip install --no-cache-dir -r requirements.txt
