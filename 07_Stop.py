import pychromecast
from pychromecast.controllers.media import MediaStatus

# Configuration
PLAYER = "All Speakers"
TIMEOUT = 5.0

# List chromecasts on the network, but don't connect
try:
    services, browser = pychromecast.discovery.discover_chromecasts()
    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)
except pychromecast.error.ChromecastConnectionError as e:
    print(f"Error discovering Chromecast devices: {e}")
    exit()

# Connect to the specified chromecast device
try:
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[PLAYER])
    cast = chromecasts[0]
    cast.wait()
except (pychromecast.error.ChromecastConnectionError, IndexError) as e:
    print(f"Error connecting to Chromecast device: {e}")
    exit()

# Get the media controller and check the status
mc = cast.media_controller
mc.block_until_active(timeout=TIMEOUT)
print(mc.status)

# Stop the media playback
mc.stop()
