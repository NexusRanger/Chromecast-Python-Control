# Ambient Chromecast Jungle - 5 channel audio stream using local test files (1 min)
import http.server
import socketserver
import threading
import pychromecast
import os
import socket

PORT = 8000  # 8000 is default
DURATION = 60 # how long to run server (sample files are only 1m long)
SERVE_DIR = r"C:\Data\Python\local" # folder containing the mp3 files 
LOCALIP = socket.gethostbyname(socket.gethostname()) # finds IP address

# Replace with a dictionary mapping Chromecast names to media filenames and volume levels
chromecast_config = {
    "Living Room Mini": ("babble.mp3"  , 0.7),
    "Kitchen Speaker" : ("jungle1.mp3" , 0.5),
    "Living Room Home": ("thunder.mp3" , 0.8),
    "Portable Speaker": ("jngbirds.mp3", 0.8),
    "Chromecast Audio": ("jungle2.mp3" , 0.7)  # add more if req
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