# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /usr/src/python-webserver

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "./main.py"]

# Build image: docker build -t python-webserver .
# Run container: docker run -d --name python-webserver -p 8000:8000 python-webserver
