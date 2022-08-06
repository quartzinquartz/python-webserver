#!/usr/bin/env python3
import requests
import http
import time
from http.server import HTTPServer
from server import Server

# HOST_NAME could be 'localhost' or DNS name where needed:
HOST_NAME = requests.get('https://checkip.amazonaws.com').text.strip() 
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - {}:{}'.format(HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - {}:{}'.format(HOST_NAME, PORT_NUMBER))

