import pychromecast
from   pychromecast.controllers.media import MediaStatus
from   pychromecast.error import ControllerNotRegistered
import pyttsx3

PLAYER = "All Speakers"    # name chromecast or group

# List chromecasts on the network, but don't connect
try:
    services, browser = pychromecast.discovery.discover_chromecasts()
    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[PLAYER])
    cast = chromecasts[0]
    cast.wait()
except (pychromecast.error.ChromecastConnectionError, IndexError) as e:
    print(f"Error connecting to Chromecast device: {e}")
    exit()

mc = cast.media_controller
engine = pyttsx3.init()
try:
    mc.block_until_active(timeout=5)
    print(mc.status)
    mc.pause()
    engine.say("Music Paused")
except ControllerNotRegistered:
    print("No media found")

engine.runAndWait()
engine.stop()
