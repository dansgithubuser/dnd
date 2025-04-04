from gpt4all import GPT4All

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def create_npc(system_message):
    model = GPT4All('gpt4all-falcon-newbpe-q4_0.gguf')
    context = model.chat_session(system_message)
    context.__enter__()
    return model, context

def serve(model, password, port=8000):
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            if self.headers.get('Authorization') != password:
                return
            content_length = int(self.headers['Content-Length'])
            question = self.rfile.read(content_length).decode()
            answer = model.generate(question)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(answer.encode())

    HTTPServer(('0.0.0.0', port), Handler).serve_forever()
