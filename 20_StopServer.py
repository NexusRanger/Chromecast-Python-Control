# Ambient Chromecast Jungle - 5 channel audio stream using local test files (1 min)
import http.server
import socketserver
import threading
import pychromecast
import os
import socket

PORT = 8000  # 8000 is default
DURATION = 3 # how long to run server (silent files are only 1s long)
SERVE_DIR = r"C:\Data\Python\local" # folder containing the mp3 files 
LOCALIP = socket.gethostbyname(socket.gethostname()) # finds IP address

# Replace with a dictionary mapping Chromecast names to media filenames and volume levels
chromecast_config = {
    "Living Room Mini": ("silent.mp3"  , 0.1),
    "Kitchen Speaker" : ("silent.mp3" , 0.1),
    "Living Room Home": ("silent.mp3" , 0.1),
    "Portable Speaker": ("silent.mp3", 0.1),
    "Chromecast Audio": ("silent.mp3" , 0.1)  # add more if req
}

CONTENT_TYPE = "audio/mp3" # content type of file

class LoggingHandler(http.server.SimpleHTTPRequestHandler):
    def log_error(self, format, *args):
        print(f"Server error: {format % args}")

os.chdir(SERVE_DIR)

Handler = LoggingHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

def start_server():
    print(f".\nStarting server on {LOCALIP} port {PORT}")
    print(f"Server will run for {DURATION} seconds")
    httpd.serve_forever()

def stop_server():
    print(".")
    httpd.shutdown()
    httpd.server_close()

server_thread = threading.Thread(target=start_server)
server_thread.start()

threading.Timer(DURATION, stop_server).start()

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=list(chromecast_config.keys()))

for cast in chromecasts:
    cast.wait() 
    mc = cast.media_controller
    filename, volume = chromecast_config[cast.name]
    cast.set_volume(volume)
    mc.play_media(f"http://{LOCALIP}:{PORT}/{filename}", CONTENT_TYPE)