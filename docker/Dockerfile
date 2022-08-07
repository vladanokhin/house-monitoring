FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list

RUN chown -R nobody:nogroup /app

RUN apt-get update

RUN pip install -r requirements.txt

# Install the mozilla firefox browser
RUN apt-get install -y --no-install-recommends firefox

