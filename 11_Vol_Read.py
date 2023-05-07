# Read Volume Level of All Chromecasts
# (Note the Vol scripts only adjust those listed in those scripts, others won't change)

import pychromecast
chromecasts, _ = pychromecast.get_chromecasts()

# Sort the chromecasts list by name
chromecasts.sort(key=lambda chromecast: chromecast.name)

# Find the maximum length of the Chromecast names
max_name_length = max(len(chromecast.name) for chromecast in chromecasts)

for chromecast in chromecasts:
    chromecast.wait()
    volume = chromecast.status.volume_level
    volume = round(volume, 1)
    # Left-justify the Chromecast name within a field of width max_name_length + 1
    name = chromecast.name.ljust(max_name_length + 1)
    print(f"{name}: {volume}")