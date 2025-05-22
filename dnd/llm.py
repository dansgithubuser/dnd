from gpt4all import GPT4All

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def create_npc(system_message):
    _tprint('creating NPC...')
    model = GPT4All('gpt4all-falcon-newbpe-q4_0.gguf')
    context = model.chat_session(system_message)
    context.__enter__()
    _tprint('done!')
    return model, context

def serve(model, password=None, port=8000):
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            if password:
                if self.headers.get('Authorization') != password:
                    return
            content_length = int(self.headers['Content-Length'])
            question = self.rfile.read(content_length).decode()
            _tprint('<<<', question)
            answer = model.generate(question)
            _tprint('>>>', answer)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(answer.encode())

    _tprint('serving...')
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()

def _tprint(*args, **kwargs):
    print(datetime.now().astimezone().isoformat(' ', 'seconds'), *args, **kwargs)
