FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list

RUN chown -R nobody:nogroup /app

RUN apt-get update

RUN pip freeze > requirements_all.txt
RUN pip uninstall -r requirements_all.txt -y

RUN pip install -r app/requirements.txt

# Install the mozilla firefox browser
RUN apt-get install -y --no-install-recommends firefox

