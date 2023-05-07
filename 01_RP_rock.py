# Play Radio Paradise Rock Stream
import pychromecast
from pychromecast.controllers.media import MediaStatus

PLAYER = "All Speakers"  # Group name

# List chromecasts on the network
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
# Discover and connect to chromecasts named *
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[PLAYER])

cast = chromecasts[0]
cast.wait()
mc = cast.media_controller
#mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
#mc.play_media('http://stream-dc1.radioparadise.com/aac-320', 'audio/flac')
#mc.play_media("http://stream.radioparadise.com/rock-flac",  "audio/flac") 
mc.play_media("http://stream.radioparadise.com/rock-128", "audio/mpeg")  

mc.block_until_active()
media_status = MediaStatus()

cast.set_volume(0.4) 
print (cast.status.volume_level)

mc.pause()
mc.play()

pychromecast.discovery.stop_discovery(browser)