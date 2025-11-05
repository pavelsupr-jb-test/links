import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World Python App</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <p>This is a simple Python web application.</p>
        </body>
        </html>
        """
        self.wfile.write(message.encode())

PORT = 8000
with socketserver.TCPServer(("0.0.0.0", PORT), HelloWorldHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
