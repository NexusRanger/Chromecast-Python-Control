import pychromecast
from pychromecast.controllers.media import MediaStatus

PLAYER = "All Speakers"

# List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()
# Shut down discovery
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[PLAYER])
cast = chromecasts[0]
cast.wait()

mc = cast.media_controller

mc.block_until_active(timeout=5)  # avoids script hanging if nothing is playing
mc.play()
print("Resuming media playback...")
