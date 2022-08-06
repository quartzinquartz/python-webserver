import os
from http.server import BaseHTTPRequestHandler
# from urllib import response
from routes.main import routes
# from pathlib import Path
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        if request_extension == "" or request_extension == ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()
        
        else:
            handler = BadRequestHandler()

        self.respond({
            'handler': handler
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()
        self.send_response(status_code)
        if status_code == 200:
            content = handler.getContents()
            self.send_header('Content-Type', handler.getContentType())
        else:
            content = "404 Not Found. <Which way did he go, George?>"
        
        self.end_headers()

        return bytes(content, "UTF-8")

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)

