from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        # Set response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Write response body
        self.wfile.write(b"Hello, Docker! This is a pure Python web app.")

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()
