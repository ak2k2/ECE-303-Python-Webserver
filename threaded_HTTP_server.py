# Nicolette Thiro, Nishat Ahmed, Armaan Kapoor - HTTP Server (threaded)

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import threading

files_in_parent_dir = os.listdir(os.path.dirname(os.path.abspath(__file__))) # get a list of all the files in the parent directory of this file

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #check if self.path is in the parent directory of this file
        if self.path[1:] in files_in_parent_dir: # self.path[1:] is the path without the leading slash
            self.send_response(200) # send a 200 OK response
            self.send_header('Content-type','text/plain') # send the content type header
            self.end_headers() # send the blank line that ends the headers
            f = open(self.path[1:]) # open the file
            self.wfile.write(f.read().encode()) # write the file to the response
            f.close() # close the file
        else:
            self.send_error(404, 'Error 404: File Not Found: %s' % self.path) # send a 404 error if the file isn't found

def serve_forever(httpd):
    httpd.serve_forever()

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8080), MyRequestHandler) # instantiate the server object with the server address and the request handler class
    threading.Thread(target=serve_forever, args=(httpd,)).start() 
    # run the server in a separate thread, so it doesn't block the main thread.
    # multiple threads can be used to run multiple servers at the same time.
    