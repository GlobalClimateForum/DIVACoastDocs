# Python-Script to start an HTTPs Server for Development
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '-1')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"Development Server running at http://localhost:{PORT}")
    httpd.serve_forever()
    
