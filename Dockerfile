FROM python:3.11.8-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install ffmpeg

COPY ./fingerprint-db ./
COPY ./readme.md ./
COPY requirements.txt ./
EXPOSE 5000
