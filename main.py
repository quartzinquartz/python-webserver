#!/usr/bin/env python3
import requests
import http
import time
from http.server import HTTPServer
from server import Server

# When containerized, '0.0.0.0' allows you to hit localhost:8000 from your host machine:
HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), f'Server UP - {HOST_NAME}:{PORT_NUMBER}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f'Server DOWN - {HOST_NAME}:{PORT_NUMBER}')

