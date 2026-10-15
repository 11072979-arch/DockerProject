import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Додаток працює успішно!"
        content = message.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

port = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", port), MyHandler)

print(f"Сервер запущено на порту {port}")
server.serve_forever()