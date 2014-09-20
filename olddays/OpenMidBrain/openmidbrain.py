import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import json

#HandlerClass = SimpleHTTPRequestHandler
#ServerClass  = BaseHTTPServer.HTTPServer
#Protocol     = "HTTP/1.0"

#if sys.argv[1:]:
#    port = int(sys.argv[1])
#else:
#    port = 8000
#server_address = ('127.0.0.1', port)

#HandlerClass.protocol_version = Protocol
#httpd = ServerClass(server_address, HandlerClass)

#sa = httpd.socket.getsockname()
#print "Serving HTTP on", sa[0], "port", sa[1], "..."
#httpd.serve_forever()

######################################## ------------------------

import string
import cgi
import cgitb
import os
import subprocess
import urllib

ContentType = 'text/plain;charset=utf-8';


class MLLHTTPSrv(SimpleHTTPRequestHandler):
    def ProcessCommand(self, reqst):
        print reqst
        r = {}
        if reqst['cmd'] == 'psth':
            r = {'type': 'PSTH'}
        return r
    
    def ProcessRequest(self, reqstr):
        rqr = {}
        reqstr = urllib.unquote(reqstr).replace('"','')
        reqstr = reqstr.partition('?')
        reqstr = reqstr[2].partition('=')
        rqr[reqstr[0]] = reqstr[2]
        print rqr
        return rqr
    
    def do_GET(self):        
        try:
            if self.path == '/':
                print self.path
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ali = {}; ali['ali'] = 'mali'; ali['hasan'] = 'gholi'; ali['path'] = self.path;
                self.wfile.write(json.dumps(ali));
            else:
                print self.path
                response = self.ProcessCommand(self.ProcessRequest(self.path))
                self.send_response(200)
                self.send_header('Content-type', ContentType);
                self.end_headers()
                #ali = {}; ali['ali'] = 'mali'; ali['hasan'] = 'gholi'; ali['path'] = self.path; ali['request'] = Request
                self.wfile.write(json.dumps(response, ensure_ascii = False));
                
                
        except IOError:
            self.send_error(404,'File Not Found: {0}'.format(self.path))

    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            length = int(self.headers['content-length'])            
            if ctype == 'text/xml':
                data = self.rfile.read(length)
                data = str(data, errors='ignore')
                self.send_response(200)
                self.send_header('Content-Type', 'text/xml')
                self.end_headers()
                
                executable = 'myexecutable'
                args = [executable, 'arg1']
                
                #comment out the line below to receive response
                subprocess.Popen(args)
                #os.spawnv(os.NO_WAIT, executable, args)

                self.wfile.write('<Response>Process is started</Response>'.encode())
                self.wfile.flush()
        except BaseException as ex:
            self.send_error(500, 'Unexpected error occured:\n{0}'.format(repr(ex)))
        print('End of do_POST')

def main():
    try:
        port = 8000
        host = '127.0.0.1'
        cgitb.enable(display=0, logdir='./log')
        server = BaseHTTPServer.HTTPServer((host, port), MLLHTTPSrv)
        print('HTTP Server is started: http://{0}:{1}/'.format(host, port))
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()
