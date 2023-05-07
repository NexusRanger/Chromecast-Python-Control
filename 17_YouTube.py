# Play a YouTube Video on a Chromecast
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

# video ID of the YouTube video to play
YOUTUBE_VIDEO_ID = "_KXU2Ob8gYY"  # _KXU2Ob8gYY sample 2 min video
PLAYER = "Shield"                 # name of your player

# Discover and connect to chromecast
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[PLAYER])
cast = chromecasts[0]
cast.wait()
yt = pychromecast.controllers.youtube.YouTubeController()
cast.register_handler(yt)
yt.play_video(YOUTUBE_VIDEO_ID)