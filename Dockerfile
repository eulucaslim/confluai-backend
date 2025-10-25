FROM python:3.11-slim

WORKDIR /conflu

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 4000