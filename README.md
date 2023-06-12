 # Chromecast-Python-Control
 Control many Chromecast functions using Python.
 Thanks to pychromecast Python library for making this all work.
 Initial setup is configured to play Radio Paradise from Main, Mellow, Rock & World streams.
 https://radioparadise.com/home (There are no adverts on these streams)
 
 But you can use any other audio (or video) streams too.
  No setup config neccessary, simply create a Chromecast group named 'All Speakers' and it should just work
 
 Python set up for Windows 10 for Python if not already installed:
  - Install Python from https://www.python.org/downloads/
  (Microsoft Store version makes a longer path)
  - Click checkbox to include Python in 'path' when installing
  - Install 'pip' from cmd window:   python -m pip install pip
  - Install 'pychromecast' from cmd window:   python -m pip install pychromecast

 Chromecase main speaker group is assumed to be named 'All Speakers'.
 Chromecast names are case sensitive
 Commands work fairly slowly, so leave plenty of time between, e.g. vol changes

 Add local mp3 files (if req) in: C:\Data\Python\local
 You can edit that path in BroadcastLocal & Jungle .py files
 (local folder only needed for local broadcast files)

 Lots of ways to execute e.g.:
  - Run the .py files on PC (Can also creat shortcuts with key combos) - Quick and easy
  - Run using HTTP request from Smartthings (Best setup as then you have control from phone, TV and Google Voice Assistant)
  - Run to test in Visual Studio Code - works well & editing is easy & visual feedback from terminal
  - Use Task Scheduler to run the .py files, e.g. to set late night vol level
  - Use TriggerCMD agent via IFTTT: https://triggercmd.com/en/
  - (From IFTTT you can use anything to trigger the scripts)
  - Use Tasker + Join from Android phone
  - Use Flirc USB with ANY IR remote control https://flirc.tv/   - works well
  - (Make shortcuts and use key combos to trigger using the Flirc USB)
  - Use Harmony Remote + Flirc USB https://harmonyhub.io/   - works very well

 #
Reddit - u/Godberd - Message with any questions

