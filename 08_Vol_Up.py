# Change Volume Level of Listed Speakers + or - on line 17
import pychromecast
chromecasts, _ = pychromecast.get_chromecasts()

volume_change = {
    "Living Room Mini": 0.1,
    "Portable Speaker": 0.1,
    "Chromecast Audio": 0.1,
    "Living Room Home": 0.1,
    "Kitchen Speaker" : 0.1
}  # volume change for each device

for chromecast in chromecasts:
    chromecast.wait()
    name = chromecast.name
    if name in volume_change:
        current_volume = chromecast.status.volume_level
        new_volume = current_volume + volume_change[name]
        chromecast.set_volume(new_volume)

# for chromecast in chromecasts:
#     chromecast.wait()
#     volume = chromecast.status.volume_level
#     volume = round(volume, 1)
#     print(f"{chromecast.name}: {volume}")