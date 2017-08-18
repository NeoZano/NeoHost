#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from urls import urls_list
from lib.file_to_show import show_page

class norse_server(BaseHTTPRequestHandler):
  def version_string(request):
    return("Norse 0.0.1")
  def log_message(self, format, *args):
        return
  def do_GET(self):
        self.send_response(200)

        for url in urls_list:
            if url[0] == self.path:
                if url[2] == 0:
                    message = url[1]()
                else:
                    file = show_page(url[1])
                    message = file[0]
                    self.send_header('Content-type',file[1])
                
                break
            else:
                file = show_page(self.path)
                message = file[0]
                self.send_header('Content-type',file[1])


        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run_server(ip='127.0.0.1',port=8080):
  print("\n-- Norse version 0.1 Alpha --\n\n")
  print('Starting server on ip '+ip+' and port '+str(port) + " ...")
  server_address = (ip, port)
  httpd = HTTPServer(server_address, norse_server)
  print('Server is now running ...\n\n')
  httpd.serve_forever()
 
