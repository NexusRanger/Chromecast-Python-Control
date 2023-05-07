# run python 'simple server' for chromecast to broadcast local file
import http.server
import socketserver
import threading
import pychromecast
import os
import socket

PORT = 8000  # change to match port number, 8000 is default
DURATION = 12 # how long to run server, though it will continue while file is playing
SERVE_DIR = r"C:\Data\Python\local"  # local mp3 files
LOCALIP = socket.gethostbyname(socket.gethostname()) # finds IP address
GROUP = "All Speakers"   # chromecast or group name
FILENAME = "HelloThisIsPythonTalking.mp3" # file to broadcast (put file in SERVE_DIR)
CONTENT_TYPE = "audio/mp3" # content type of file
VOLUME = 0.6

# # Will also play mp4 files to video cc. (or send to speakers & will play the audio)
#FILENAME = "BigBuckBunny.mp4" # file to broadcast (put file in SERVE_DIR)
#CONTENT_TYPE = "video/mp4" # content type of file

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
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[GROUP])

cast = chromecasts[0]
cast.wait() 

mc = cast.media_controller

mc.play_media(f"http://{LOCALIP}:{PORT}/{FILENAME}", content_type=CONTENT_TYPE)

mc.block_until_active()

cast.set_volume(VOLUME) 
print("Group: '"+GROUP+"'" + " Volume: " + str(round(cast.status.volume_level, 1)))