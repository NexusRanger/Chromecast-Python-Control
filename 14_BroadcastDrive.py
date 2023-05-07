# Play an mp3 Audio File from Google Drive
import pychromecast
from pychromecast.controllers.media import MediaStatus

GROUP = "All Speakers"   # chromecase name or group

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[GROUP])

cast = chromecasts[0]
cast.wait() 

mc = cast.media_controller
mc.play_media("https://docs.google.com/uc?id=1ljUV1VSUcs21kYxoApNab2Uz7Td1bfF0&", "audio/mp3")
# to play a file from google drive, share the containing folder, then use the file ID as above
# will also work with mp4 video, plays audio over speakers
# this uses the same sample mp3 file as for local, but this copy is in Google Drive

mc.block_until_active()
media_status = MediaStatus()

cast.set_volume(0.6) 
print ("Volume: " + str(round(cast.status.volume_level, 1)))
