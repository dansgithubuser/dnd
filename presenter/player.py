import pyglet

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from urllib.parse import parse_qs, urlparse

#===== consts =====#
PORT = 8000

#===== file-scope variables =====#
class F:
    window = pyglet.window.Window(
        width=600,
        height=480,
        caption='presenter',
        resizable=True,
        vsync=True,
    )
    sprite = None
    request = None

#===== server =====#
class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        req = urlparse(self.path)
        query = parse_qs(req.query)
        match req.path:
            case '/fullscreen':
                F.request = 'fullscreen'
            case '/present':
                F.request = ('present', query['path'][0])
            case _:
                self.send_error(404)
                return
        self.send_response(204)
        self.end_headers()

def serve():
    HTTPServer(('127.0.0.1', 8000), HttpHandler).serve_forever()

#===== GUI =====#
def update(_delta):
    if not F.request: return
    try:
        match F.request:
            case 'fullscreen':
                F.window.set_fullscreen(not F.window.fullscreen)
            case 'present', path:
                img = pyglet.image.load(path)
                img.anchor_x = img.width // 2
                img.anchor_y = img.height // 2
                F.sprite = pyglet.sprite.Sprite(img)
    except Exception as e:
        print(e)
    F.request = None

@F.window.event
def on_draw():
    F.window.clear()
    if F.sprite:
        F.sprite.x = F.window.width / 2
        F.sprite.y = F.window.height / 2
        F.sprite.scale = min(
            F.window.width / F.sprite.image.width,
            F.window.height / F.sprite.image.height,
        )
        F.sprite.draw()

#===== main =====#
def main(args):
    threading.Thread(target=serve, daemon=True).start()
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
