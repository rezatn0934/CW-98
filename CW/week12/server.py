from http.server import HTTPServer, BaseHTTPRequestHandler
import json
HOST = "127.0.0.1"
PORT = 999

database = dict()


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(database).encode())

    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            unique_key = str(len(database) + 1)
            database[unique_key] = json.loads(data.decode())
            self.send_response(201)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Successful")


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("server now running...")

server.serve_forever()
# server.server_close()
# print("Server stopped!")