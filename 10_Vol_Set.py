# Set Volume for Each Chromecast by Name
import pychromecast

chromecasts, _ = pychromecast.get_chromecasts()
volume_levels = {
"Bedroom Speaker 1" : 0.2,
"Chromecast Audio"  : 0.5,
"Kitchen Speaker"   : 0.4,
"Living Room Home"  : 0.3,
"Living Room Mini"  : 0.4,
"Portable Speaker"  : 0.5,
"Showerroom Speaker": 0.3
}  

# set volumes
for chromecast in chromecasts:
    chromecast.wait()
    name = chromecast.name
    if name in volume_levels:
        volume = volume_levels[name]
        chromecast.set_volume(volume)

# Read and print the volume levels for each Chromecast as a check
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

# If you see any levels not responding correctly check for typos/case in chromecast names