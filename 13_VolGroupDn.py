# Change Volume Level of group
import pychromecast

chromecasts, _ = pychromecast.get_chromecasts()

PLAYER = "All Speakers"
LEVEL = -0.1

volume_change = {PLAYER:LEVEL}

for chromecast in chromecasts:
    chromecast.wait()
    name = chromecast.name
    if name in volume_change:
        current_volume = chromecast.status.volume_level
        new_volume = current_volume + volume_change[name]
        if new_volume < 0.0:
            print(f"Error: New volume level for {name} is below minimum value")
            new_volume = 0.0
        elif new_volume > 1.0:
            print(f"Error: New volume level for {name} is above maximum value")
            new_volume = 1.0
        chromecast.set_volume(new_volume)

'''
When you create a Chromecast group, the volume level of the group is initially 
set to the average volume level of all the devices in the group. 
Adjusting the volume level of the group will change the volume level of 
all the devices in the group by the same amount. For example, 
if you increase the volume level of the group by 10%, the volume level 
of each device in the group will also increase by 10%.

Adjusting the volume level of an individual device in a Chromecast group 
will only affect that device and will not change the volume level of the group 
or any other devices in the group. However, if you adjust the volume level of an 
individual device and then adjust the volume level of the group, 
the volume level of all devices in the group will be changed relative 
to their current volume levels.

In summary, adjusting the volume level of a Chromecast group changes the volume
level of all devices in the group by the same amount, 
while adjusting the volume level of an individual device only affects that device.
'''