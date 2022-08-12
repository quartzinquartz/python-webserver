import os
from response.requestHandler import RequestHandler

class StaticHandler(RequestHandler):
    def __init__(self):
        self.filetypes = {
            '.js': 'text/javascript',
            '.css': 'text/css',
            '.jpg': 'image/jpeg',
            '.png': 'image/png',
            'notfound': 'text/plain'
        }

    def find(self, file_path):
        split_path = os.path.splitext(file_path)
        file_extension = split_path[1]

        try:
            # NOTE:
            # - It would be wise to logicically prevent '..' from being in the request path.
            #   Because that could take one to a directory level above where they should be.
            if file_extension in ('.jpg', '.jpeg', '.png'):
                self.contents = open(f'public{file_path}', 'rb')
            else:
                self.contents = open(f'public{file_path}', 'r')

            self.setContentType(file_extension)
            self.setStatus(200)
            return True

        # NOTE: This bare-bones error handling could be much improved.
        except:
            self.setContentType('notfound')
            self.setStatus(404)
            return False

    def setContentType(self, ext):
        self.contentType = self.filetypes[ext]
